import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm


def clean_text(text):
    """Supprime les phrases de chat que le LLM ajoute parfois (Voici..., Je ne trouve...)."""
    parasites = [
        r"^voici.*$",
        r"^je ne trouve(rai)? (pas|plus).*$",
        r"^d'accord.*$",
        r"^bien s[uû]r.*$",
        r"^voil[aà].*$",
    ]
    cleaned = []
    for line in text.split("\n"):
        stripped = line.strip()
        if any(re.match(p, stripped, re.IGNORECASE) for p in parasites):
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip()


def parse_markdown_table(block_lines):
    """Convertit des lignes markdown '| a | b |' en liste de listes pour reportlab.Table."""
    rows = []
    for line in block_lines:
        if re.match(r"^\|?[\s\-:\|]+\|?$", line):
            continue  # ligne séparatrice |---|---|
        cells = [c.strip().replace("**", "") for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    return rows


def generate_pdf(text, filename="rapport.pdf", title="DDoS Security Assistant Report"):
    text = clean_text(text)

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        topMargin=2 * cm, bottomMargin=2 * cm,
        leftMargin=2 * cm, rightMargin=2 * cm,
    )
    styles = getSampleStyleSheet()
    body_style = ParagraphStyle(
        "BodyJustified", parent=styles["BodyText"], alignment=4, spaceAfter=8, leading=14
    )

    content = [Paragraph(title, styles["Title"]), Spacer(1, 20)]

    lines = text.split("\n")
    buffer = []
    table_buffer = []
    in_table = False

    def flush_paragraph():
        if buffer:
            paragraph_text = " ".join(buffer).strip()
            if paragraph_text:
                content.append(Paragraph(paragraph_text, body_style))
                content.append(Spacer(1, 10))
            buffer.clear()

    def flush_table():
        if table_buffer:
            data = parse_markdown_table(table_buffer)
            if data:
                cell_style = ParagraphStyle("Cell", parent=styles["BodyText"], fontSize=8, leading=10)
                header_style = ParagraphStyle("CellHeader", parent=cell_style, textColor=colors.white, fontName="Helvetica-Bold")
                wrapped = []
                for r_idx, row in enumerate(data):
                    style_to_use = header_style if r_idx == 0 else cell_style
                    wrapped.append([Paragraph(cell, style_to_use) for cell in row])

                table = Table(wrapped, hAlign="LEFT", repeatRows=1)
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2c3e50")),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f5f5f5")]),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]))
                content.append(table)
                content.append(Spacer(1, 16))
            table_buffer.clear()

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("#"):
            flush_paragraph(); flush_table()
            level = len(stripped) - len(stripped.lstrip("#"))
            heading_text = stripped.lstrip("#").strip()
            style = styles["Heading1"] if level == 1 else styles["Heading2"]
            content.append(Paragraph(heading_text, style))
            content.append(Spacer(1, 8))
            continue

        if stripped.startswith("|"):
            if not in_table:
                flush_paragraph()
                in_table = True
            table_buffer.append(stripped)
            continue
        else:
            if in_table:
                flush_table()
                in_table = False

        if stripped == "":
            flush_paragraph()
            continue

        buffer.append(stripped)

    flush_paragraph(); flush_table()
    doc.build(content)
    return filename