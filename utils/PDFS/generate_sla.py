"""Generate AccuKnox SaaS Service Level Agreement PDF."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    Image, HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT_PATH = r"D:\Atharva\AccuKnox\HelpDocs\utils\PDFS\AccuKnox_SaaS_SLA.pdf"
LOGO_PATH = r"D:\Atharva\AccuKnox\HelpDocs\docs\assets\images\ak-logo.png"

ACCUKNOX_BLUE = colors.HexColor("#1B6FC8")
DARK_GRAY = colors.HexColor("#333333")
LIGHT_GRAY = colors.HexColor("#F5F5F5")
TABLE_HEADER_BG = colors.HexColor("#1B6FC8")
TABLE_BORDER = colors.HexColor("#CCCCCC")

def page_header_footer(canvas, doc):
    canvas.saveState()
    width, height = letter

    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#666666"))

    page_num = doc.page
    total_pages = 2
    canvas.drawString(inch, 0.55 * inch, f"Page {page_num} of {total_pages}")
    canvas.drawRightString(width - inch, 0.55 * inch, "Last Updated May 13, 2026")

    canvas.setStrokeColor(colors.HexColor("#DDDDDD"))
    canvas.setLineWidth(0.5)
    canvas.line(inch, 0.7 * inch, width - inch, 0.7 * inch)

    canvas.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        rightMargin=inch,
        leftMargin=inch,
        topMargin=0.75 * inch,
        bottomMargin=inch,
    )

    styles = getSampleStyleSheet()

    style_normal = ParagraphStyle(
        "ak_normal",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=15,
        textColor=DARK_GRAY,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
    )
    style_heading1 = ParagraphStyle(
        "ak_h1",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=DARK_GRAY,
        spaceBefore=14,
        spaceAfter=6,
    )
    style_doc_title = ParagraphStyle(
        "ak_doc_title",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        textColor=DARK_GRAY,
        alignment=TA_CENTER,
        spaceBefore=6,
        spaceAfter=14,
    )
    style_list_item = ParagraphStyle(
        "ak_list",
        parent=style_normal,
        leftIndent=20,
        spaceAfter=4,
    )
    style_list_sub = ParagraphStyle(
        "ak_list_sub",
        parent=style_normal,
        leftIndent=40,
        spaceAfter=4,
    )
    style_definition = ParagraphStyle(
        "ak_def",
        parent=style_normal,
        leftIndent=20,
        spaceAfter=6,
    )
    style_effective = ParagraphStyle(
        "ak_effective",
        parent=styles["Normal"],
        fontName="Helvetica-BoldOblique",
        fontSize=10,
        leading=14,
        textColor=DARK_GRAY,
        spaceBefore=24,
    )

    story = []

    # ── Logo ──
    if os.path.exists(LOGO_PATH):
        logo = Image(LOGO_PATH, width=2.4 * inch, height=0.65 * inch, kind="proportional")
        logo.hAlign = "CENTER"
        story.append(logo)
    else:
        story.append(Paragraph(
            '<font name="Helvetica-Bold" size="24" color="#1B6FC8">AccuKnox</font>',
            ParagraphStyle("logo_text", alignment=TA_CENTER, spaceAfter=4)
        ))

    story.append(Spacer(1, 10))

    # ── Horizontal rule ──
    story.append(HRFlowable(width="100%", thickness=1.5, color=ACCUKNOX_BLUE, spaceAfter=10))

    # ── Document Title ──
    story.append(Paragraph("ACCUKNOX SAAS SERVICE LEVEL AGREEMENT", style_doc_title))

    # ── Preamble ──
    story.append(Paragraph(
        'This AccuKnox, Inc. ("<b>AccuKnox</b>") SaaS Service Level Agreement ("<b>SLA</b>") applies to each '
        'end customer entitled to use paid AccuKnox SaaS (each a "<b>Customer</b>"), unless separate '
        'product-specific SLAs are listed at <link href="https://www.accuknox.com/agreements" '
        'color="#1B6FC8"><u>https://www.accuknox.com/agreements</u></link>, in which case those '
        'product-specific SLAs govern for that applicable paid SaaS Services Entitlement. In the event of a '
        'conflict between this SLA and the SaaS Terms of Service (the "<b>Terms</b>"), the terms and conditions '
        'of this SLA apply, but only to the extent of such conflict. Capitalized terms used but not defined '
        'herein shall have their meaning set forth in the Terms.',
        style_normal,
    ))

    # ── Section 1 ──
    story.append(Spacer(1, 6))
    story.append(Paragraph("1.&nbsp;&nbsp;&nbsp;SERVICE COMMITMENT", style_heading1))
    story.append(Paragraph(
        'AccuKnox has designed its SaaS Services with a goal of providing access 100% of the time. As with '
        'any SaaS service, very rare and occasional circumstances may result in temporary loss of use. '
        'AccuKnox will make every effort to avoid such occurrence and to minimize their impact when they do '
        'occur. As further assurance, AccuKnox makes the following commitment:',
        style_normal,
    ))
    story.append(Paragraph(
        'During Customer’s applicable SaaS subscription, AccuKnox will make the relevant SaaS Service '
        'Available during each calendar month as described below (the "<b>Service Commitment</b>"). In the '
        'event the subscribed SaaS Service does not meet the Service Commitment, Customer will be eligible '
        'to receive a Service Credit as described herein.',
        style_normal,
    ))

    # ── Section 2 ──
    story.append(Spacer(1, 6))
    story.append(Paragraph("2.&nbsp;&nbsp;&nbsp;SERVICE CREDITS", style_heading1))
    story.append(Paragraph(
        'Service Credits arise in any calendar month in which the Monthly Uptime Percentage falls within the '
        'ranges set forth in the table below.',
        style_normal,
    ))
    story.append(Spacer(1, 6))

    # Credits table
    table_data = [
        [
            Paragraph("<b>Monthly Uptime Percentage</b>", ParagraphStyle(
                "th", fontName="Helvetica-Bold", fontSize=10, textColor=colors.white,
                alignment=TA_CENTER, leading=14)),
            Paragraph("<b>Service Credit Percentage</b>", ParagraphStyle(
                "th", fontName="Helvetica-Bold", fontSize=10, textColor=colors.white,
                alignment=TA_CENTER, leading=14)),
        ],
        [
            Paragraph("Less than 99.9% but greater than or equal to 99.0%", style_normal),
            Paragraph("10%", ParagraphStyle("td_c", parent=style_normal, alignment=TA_CENTER)),
        ],
        [
            Paragraph("Less than 99.0% but greater than or equal to 95.0%", style_normal),
            Paragraph("25%", ParagraphStyle("td_c", parent=style_normal, alignment=TA_CENTER)),
        ],
        [
            Paragraph("Less than 95.0%", style_normal),
            Paragraph("100%", ParagraphStyle("td_c", parent=style_normal, alignment=TA_CENTER)),
        ],
    ]

    col_widths = [3.8 * inch, 2.1 * inch]
    tbl = Table(table_data, colWidths=col_widths, hAlign="CENTER")
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
        ("GRID", (0, 0), (-1, -1), 0.5, TABLE_BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        'Service Credits are calculated as a specified percentage of an additional equivalent capacity month '
        'for the applicable SaaS Service(s) affected (rounded to the nearest number of whole calendar months) '
        '(any such month, an "<b>Extension Month</b>").',
        style_normal,
    ))
    story.append(Paragraph(
        'For example, if the Monthly Uptime Percentage fell to 98.9% in any two (2) particular calendar '
        'months during a one (1) year subscription, then the aggregate Service Credit would be calculated as '
        '50% which would be rounded up to one (1) Extension Month of equivalent service and capacity added to '
        'the end of the subscription period without cost to the Customer.',
        style_normal,
    ))

    # ── Section 3 ──
    story.append(Spacer(1, 6))
    story.append(Paragraph("3.&nbsp;&nbsp;&nbsp;CREDIT REQUEST AND PAYMENT PROCEDURES", style_heading1))
    story.append(Paragraph(
        'In order to receive a Service Credit, Customer must submit a claim by opening a case with AccuKnox '
        'technical support within thirty (30) days after the end of the calendar month during which the '
        'Service Commitment was not met, and must include: (i) the words “SLA Credit Request” in the '
        'subject line; (ii) the calendar month for which Customer is claiming Service Credits together with the '
        'dates and times of each incident of claimed non-Availability; and (iii) logs or other information '
        'evidencing the failure to meet the Service Commitment (any confidential or sensitive information '
        'should be removed or redacted). Customer’s failure to provide the request and information required '
        'above will disqualify Customer from receiving a Service Credit.',
        style_normal,
    ))
    story.append(Paragraph(
        'If AccuKnox confirms the Service Commitment was not met, then AccuKnox will issue Customer a note '
        'confirming that we will apply the applicable Service Credit towards an Extension Month.',
        style_normal,
    ))

    # ── Page Break ──
    story.append(PageBreak())

    # ── Logo on page 2 ──
    if os.path.exists(LOGO_PATH):
        logo2 = Image(LOGO_PATH, width=2.4 * inch, height=0.65 * inch, kind="proportional")
        logo2.hAlign = "CENTER"
        story.append(logo2)
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=ACCUKNOX_BLUE, spaceAfter=14))

    # ── Section 4 ──
    story.append(Paragraph("4.&nbsp;&nbsp;&nbsp;MAXIMUM CREDITS; DISPUTE RESOLUTION", style_heading1))
    story.append(Paragraph(
        'Service Credits will not entitle Customer to any refund or other payment from AccuKnox. Service '
        'Credits may not be transferred or applied to any other account.',
        style_normal,
    ))
    story.append(Paragraph(
        'The aggregate maximum number of Service Credits to be issued to Customer in a single annual '
        'subscription period will not exceed three (3) Extension Months. This SLA states Customer’s sole '
        'and exclusive remedy for any failure by AccuKnox to meet the Service Commitment.',
        style_normal,
    ))
    story.append(Paragraph(
        'If a dispute arises with respect to this SLA, AccuKnox will make a determination in good faith based '
        'on its system logs, monitoring reports, configuration records, and other available information, '
        'relevant portions of which AccuKnox will make available for review by Customer at Customer’s '
        'reasonable written request on a case-by-case basis from time to time, subject to appropriate privacy '
        'and security protections.',
        style_normal,
    ))

    # ── Section 5 ──
    story.append(Spacer(1, 6))
    story.append(Paragraph("5.&nbsp;&nbsp;&nbsp;SLA EXCLUSIONS", style_heading1))
    story.append(Paragraph("The Service Commitment does not apply to:", style_normal))

    story.append(Paragraph(
        "a)&nbsp;&nbsp;Beta products or other features expressly excluded from the SLA (in associated Documentation);",
        style_list_item,
    ))
    story.append(Paragraph(
        "b)&nbsp;&nbsp;Maintenance Downtime; or",
        style_list_item,
    ))
    story.append(Paragraph(
        "c)&nbsp;&nbsp;unavailability of, or other issues with, the SaaS Services caused by or resulting from:",
        style_list_item,
    ))
    story.append(Paragraph(
        "i.&nbsp;&nbsp;&nbsp;&nbsp;factors outside AccuKnox’s reasonable control;",
        style_list_sub,
    ))
    story.append(Paragraph(
        "ii.&nbsp;&nbsp;&nbsp;actions or inactions of Customer or any third party acting on Customer’s behalf;",
        style_list_sub,
    ))
    story.append(Paragraph(
        "iii.&nbsp;&nbsp;Customer’s (or third-party supplied) equipment, connectivity, software or hardware; or",
        style_list_sub,
    ))
    story.append(Paragraph(
        'iv.&nbsp;&nbsp;abuses or other behaviors that violate this SLA or the Terms (collectively, the "<b>SLA Exclusions</b>").',
        style_list_sub,
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "If Availability is impacted by other factors, we may issue a Service Credit at our discretion.",
        style_normal,
    ))

    # ── Section 6 ──
    story.append(Spacer(1, 6))
    story.append(Paragraph("6.&nbsp;&nbsp;&nbsp;DEFINITIONS", style_heading1))

    story.append(Paragraph(
        'a)&nbsp;&nbsp;"<b>Available</b>" and "<b>Availability</b>" means that Customer can log in to the '
        'SaaS Services through <link href="https://app.accuknox.com" color="#1B6FC8">'
        '<u>https://app.accuknox.com</u></link>, as measured by AccuKnox via testing agents that report the '
        'current state and availability of the SaaS Services every sixty (60) seconds. When there is a known '
        'Availability issue, Customer can view status at '
        '<link href="https://status.accuknox.com" color="#1B6FC8"><u>https://status.accuknox.com</u></link>.',
        style_definition,
    ))
    story.append(Paragraph(
        'b)&nbsp;&nbsp;"<b>Maintenance Downtime</b>" means Scheduled Downtime and Emergency Downtime.',
        style_definition,
    ))
    story.append(Paragraph(
        'c)&nbsp;&nbsp;"<b>Monthly Uptime Percentage</b>" means the total number of minutes of Availability in '
        'a month divided by the total number of minutes in a month, in both cases excluding Maintenance Downtime.',
        style_definition,
    ))
    story.append(Paragraph(
        'd)&nbsp;&nbsp;"<b>Scheduled Downtime</b>" means a scheduled period of time for maintenance and upgrade '
        'activity during which the SaaS Service is not Available and which is preceded by not less than twelve '
        '(12) to twenty-four (24) hours written warning from AccuKnox (via AccuKnox’s normal SaaS '
        'communication channels).',
        style_definition,
    ))
    story.append(Paragraph(
        'e)&nbsp;&nbsp;A "<b>Service Credit</b>" is an entitlement to a percentage of an Extension Month as '
        'described in Section 2.',
        style_definition,
    ))
    story.append(Paragraph(
        'f)&nbsp;&nbsp;"<b>Emergency Downtime</b>" means unannounced periods of time for emergency maintenance '
        'and upgrade activity during which the SaaS Service is not Available, not exceeding one (1) hour per '
        'calendar month in total.',
        style_definition,
    ))

    # ── Effective date ──
    story.append(Paragraph("Effective May 13, 2026", style_effective))

    doc.build(story, onFirstPage=page_header_footer, onLaterPages=page_header_footer)
    print(f"PDF saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
