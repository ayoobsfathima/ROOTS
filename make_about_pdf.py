"""
Builds the one-page "About Roots" PDF, a plain-language explainer for the
Roots trajectory-explorer web app.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

TEAL = HexColor("#1FA98C")
TEAL_DEEP = HexColor("#0E5B49")
PINK = HexColor("#F6B8C4")
PINK_DARK = HexColor("#D56E86")
INK = HexColor("#16221e")
INK_SOFT = HexColor("#3f5650")
INK_MUTED = HexColor("#7c9089")
BG_SOFT = HexColor("#F6FAF8")
BG_PINK = HexColor("#FFF7F8")

PAGE_W, PAGE_H = A4
MARGIN = 14 * mm

doc = SimpleDocTemplate(
    "assets/about-roots.pdf",
    pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=10 * mm, bottomMargin=10 * mm,
    title="About Roots", author="Roots project",
)

styles = getSampleStyleSheet()

# Times New Roman: the standard PDF base font "Times-Roman" family maps to
# Times New Roman on Windows viewers and a metrically compatible serif
# elsewhere, and is built into every PDF reader (no font embedding needed).
FONT = "Times-Roman"
FONT_BOLD = "Times-Bold"
FONT_ITALIC = "Times-Italic"

title_style = ParagraphStyle(
    "RootsTitle", parent=styles["Title"], fontName=FONT_BOLD,
    fontSize=20, leading=23, textColor=TEAL_DEEP, spaceAfter=6, alignment=TA_LEFT,
)
h2_style = ParagraphStyle(
    "H2", parent=styles["Heading2"], fontName=FONT_BOLD,
    fontSize=12.5, leading=15, textColor=TEAL_DEEP, spaceBefore=7, spaceAfter=3,
)
body_style = ParagraphStyle(
    "Body", parent=styles["Normal"], fontName=FONT,
    fontSize=12, leading=14.5, textColor=INK, spaceAfter=3,
)
bullet_style = ParagraphStyle(
    "Bullet", parent=body_style, leftIndent=14, bulletIndent=2, spaceAfter=3,
)
small_muted = ParagraphStyle(
    "SmallMuted", parent=styles["Normal"], fontName=FONT,
    fontSize=8.5, leading=11, textColor=INK_MUTED,
)

def bullets(items):
    return [Paragraph("&bull;&nbsp;&nbsp;" + t, bullet_style) for t in items]

story = []

# ---- Header ----
story.append(Paragraph("Roots", ParagraphStyle(
    "Logo", fontName=FONT_BOLD, fontSize=15, textColor=PINK_DARK,
    spaceAfter=2,
)))
story.append(Paragraph("About the model", title_style))
story.append(HRFlowable(width="100%", thickness=1.3, color=TEAL, spaceAfter=8))

# ---- What is this ----
story.append(Paragraph("What is Roots?", h2_style))
story.append(Paragraph(
    "Roots applies a method called <b>Disease Course Mapping</b>, originally developed to track how "
    "Parkinson's disease progresses over time, to autism severity scores instead. Given a handful of visits "
    "for a child, it estimates where that child sits on a shared developmental timeline and how quickly they are "
    "moving along it, then predicts their likely trajectory on each item of the <b>CARS2-ST</b> severity scale.",
    body_style,
))

# ---- How it was built ----
story.append(Paragraph("How it was built", h2_style))
story.append(Paragraph(
    "The underlying statistics come from Poulet and Durrleman (2023, <i>Statistics in Medicine</i>), who built this "
    "method for a Parkinson's scale with 59 items (MDS UPDRS). Roots reuses the same model for the CARS2-ST scale, "
    "which has 15 items.",
    body_style,
))
story.append(Spacer(1, 2))
story.extend(bullets([
    "No real longitudinal CARS2-ST dataset was available, so the model was trained on <b>realistic synthetic data</b> "
    "(300 simulated children), generated to match published score ranges and the three factor structure of "
    "CARS2-ST, as published by Campbell et al. (2026): Social Communication, Restrictive/Repetitive Behavior and "
    "Sensory, and Emotional/Behavioral Dysregulation.",
    "For each item, the model learns a <b>population average curve</b>: how scores typically change with age.",
    "For each child, it then estimates two personal dials from their actual visit scores, <b>pace</b> "
    "(faster or slower than average) and <b>timing</b> (earlier or later start), and uses those to shift the "
    "population curve into a personalized one.",
]))

# ---- Pros / Cons table ----
story.append(Paragraph("Pros and cons", h2_style))

pros_items = [
    "Reuses a rigorous method validated on real neurodegenerative disease data, applied here to a new domain.",
    "Naturally handles irregular visit schedules, few visits per child, and ranked (ordinal) scores.",
    "Gives an interpretable personal summary (pace and timing), not just a single severity number.",
    "Captures the CARS2-ST's published three factor severity structure.",
]
cons_items = [
    "Trained on synthetic, not real patient, data: a proof of concept, not a validated clinical tool.",
    "Assumes severity moves in <b>one direction</b> per item, so it cannot show a child worsening on one item "
    "while improving on another within the same run.",
    "At smaller sample sizes the model struggles to cleanly separate the three severity factors, "
    "a known limitation found during testing.",
    "Needs real longitudinal CARS2-ST data to properly validate before any clinical use.",
]

pros_flow = [Paragraph("<b>Pros</b>", ParagraphStyle(
    "ProsHead", parent=body_style, textColor=TEAL_DEEP, fontName=FONT_BOLD, fontSize=12.5, spaceAfter=5))]
pros_flow += bullets(pros_items)
cons_flow = [Paragraph("<b>Cons and limitations</b>", ParagraphStyle(
    "ConsHead", parent=body_style, textColor=PINK_DARK, fontName=FONT_BOLD, fontSize=12.5, spaceAfter=5))]
cons_flow += bullets(cons_items)

pc_table = Table([[pros_flow, cons_flow]], colWidths=[(PAGE_W - 2*MARGIN) / 2.0 - 4, (PAGE_W - 2*MARGIN) / 2.0 - 4])
pc_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BACKGROUND", (0, 0), (0, 0), BG_SOFT),
    ("BACKGROUND", (1, 0), (1, 0), BG_PINK),
    ("BOX", (0, 0), (0, 0), 0.8, TEAL),
    ("BOX", (1, 0), (1, 0), 0.8, PINK_DARK),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
]))
story.append(pc_table)

# ---- How to use ----
story.append(Paragraph("How to use and interpret it", h2_style))
story.extend(bullets([
    "Enter the child's age and CARS2-ST item scores for each visit in the <b>Trajectory Explorer</b>.",
    "After at least one visit, the tool shows <b>Developmental pace</b> (1.00x means exactly average pace; "
    "higher or lower means faster or slower than the population average) and <b>Timing offset</b> "
    "(how many years earlier or later this child started, relative to average).",
    "Pick any item from the dropdown to see this child's personalized curve (solid teal line) against the "
    "population average (dashed grey line), with recorded visits shown as dots.",
    "Treat the curves as an illustration of how the method works, not as a prediction to act on. "
    "This is a demonstration built on synthetic data, not a diagnostic or clinical decision support tool.",
]))

story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=0.7, color=HexColor("#dde8e3"), spaceAfter=5))
story.append(Paragraph(
    "Reference: Poulet, P. E. and Durrleman, S. (2023). Multivariate disease progression modelling with "
    "longitudinal ordinal data. <i>Statistics in Medicine</i>. &nbsp;|&nbsp; "
    "CARS2-ST factor structure: Campbell et al. (2026). &nbsp;|&nbsp; "
    "CARS2-ST item content, copyright Schopler et al., 2010 (WPS), is not reproduced in this tool.",
    small_muted,
))

doc.build(story)
print("Wrote assets/about-roots.pdf")
