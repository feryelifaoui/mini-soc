import os
import json
from datetime import datetime
from typing import List, Dict, Any, Optional

from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

# Configuration DB (PostgreSQL par défaut, fallback SQLite pour simplicité de dev local)
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:postgres@localhost:5432/mini_soc"
)

Base = declarative_base()

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    attack_type = Column(String(100), nullable=False)
    confidence = Column(Float, nullable=False)
    confidence_level = Column(String(50), nullable=False)
    flow_features = Column(Text, nullable=True)
    status = Column(String(50), default="Nouveau")

    tickets = relationship("Ticket", back_populates="incident", cascade="all, delete-orphan")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S") if self.timestamp else None,
            "attack_type": self.attack_type,
            "confidence": self.confidence,
            "confidence_level": self.confidence_level,
            "flow_features": json.loads(self.flow_features) if self.flow_features else {},
            "status": self.status
        }

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    incident_id = Column(Integer, ForeignKey("incidents.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    priority = Column(String(50), default="Haute")
    status = Column(String(50), default="Ouvert")
    assigned_to = Column(String(100), default="SOC Analyst")
    created_at = Column(DateTime, default=datetime.utcnow)

    incident = relationship("Incident", back_populates="tickets")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "incident_id": self.incident_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.created_at else None
        }

def get_db_engine():
    """Crée le moteur SQLAlchemy avec tentative PostgreSQL, sinon SQLite."""
    try:
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        # Test connexion rapide
        with engine.connect() as conn:
            pass
        return engine
    except Exception as e:
        error_msg = str(e)
        try:
            print(f"[!] Impossible de se connecter a PostgreSQL ({error_msg}). Utilisation de SQLite en fallback local.")
        except Exception:
            print("[!] Impossible de se connecter a PostgreSQL. Utilisation de SQLite en fallback local.")
        sqlite_url = "sqlite:///./mini_soc.db"
        return create_engine(sqlite_url, connect_args={"check_same_thread": False})

engine = get_db_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialise les tables dans la BDD si elles n'existent pas."""
    Base.metadata.create_all(bind=engine)

def get_db_session():
    """Générateur de session DB pour FastAPI / Services."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ── helpers CRUD ──────────────────────────────────────────────────────────

def create_incident_db(
    attack_type: str, 
    confidence: float, 
    confidence_level: str, 
    flow_features: dict,
    status: str = "Nouveau"
) -> Incident:
    db = SessionLocal()
    try:
        incident = Incident(
            attack_type=attack_type,
            confidence=confidence,
            confidence_level=confidence_level,
            flow_features=json.dumps(flow_features),
            status=status
        )
        db.add(incident)
        db.commit()
        db.refresh(incident)
        return incident
    finally:
        db.close()

def create_ticket_db(
    incident_id: int,
    title: str,
    description: str,
    priority: str = "Haute",
    status: str = "Ouvert",
    assigned_to: str = "SOC Analyst"
) -> Ticket:
    db = SessionLocal()
    try:
        ticket = Ticket(
            incident_id=incident_id,
            title=title,
            description=description,
            priority=priority,
            status=status,
            assigned_to=assigned_to
        )
        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return ticket
    finally:
        db.close()

def get_all_incidents_db(limit: int = 100) -> List[Dict[str, Any]]:
    db = SessionLocal()
    try:
        incidents = db.query(Incident).order_by(Incident.timestamp.desc()).limit(limit).all()
        return [inc.to_dict() for inc in incidents]
    finally:
        db.close()

def get_all_tickets_db(limit: int = 100) -> List[Dict[str, Any]]:
    db = SessionLocal()
    try:
        tickets = db.query(Ticket).order_by(Ticket.created_at.desc()).limit(limit).all()
        return [t.to_dict() for t in tickets]
    finally:
        db.close()

def get_dashboard_stats_db() -> Dict[str, Any]:
    db = SessionLocal()
    try:
        total_incidents = db.query(Incident).count()
        total_tickets = db.query(Ticket).count()
        
        avg_confidence_res = db.query(Incident).all()
        avg_conf = (
            sum(i.confidence for i in avg_confidence_res) / len(avg_confidence_res) 
            if avg_confidence_res else 0.0
        )
        
        # Statut distribution
        status_counts = {}
        for inc in avg_confidence_res:
            status_counts[inc.status] = status_counts.get(inc.status, 0) + 1
            
        return {
            "total_incidents": total_incidents,
            "total_tickets": total_tickets,
            "avg_confidence": round(avg_conf, 4),
            "status_distribution": status_counts
        }
    finally:
        db.close()


def update_incident_status_db(incident_id: int, new_status: str) -> Optional[Dict[str, Any]]:
    db = SessionLocal()
    try:
        incident = db.query(Incident).filter(Incident.id == incident_id).first()
        if not incident:
            return None
        incident.status = new_status
        # Mettre à jour aussi le ticket associé si présent
        ticket = db.query(Ticket).filter(Ticket.incident_id == incident_id).first()
        if ticket:
            ticket.status = "Résolu" if new_status == "Résolu" else ("En cours" if new_status == "En cours" else "Ouvert")
        db.commit()
        db.refresh(incident)
        return incident.to_dict()
    finally:
        db.close()

