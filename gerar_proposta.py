# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)

OUT = r"C:\Users\rafam\Desktop\Rpositórios Github - claude\Pessoal\Viagem China\Proposta Viagem China - Pequim e Harbin.pdf"

# ---- paleta ----
INK      = colors.HexColor("#1f2937")
MUTED    = colors.HexColor("#6b7280")
GOLD     = colors.HexColor("#805602")
GOLD_BG  = colors.HexColor("#fbf3e2")
RED      = colors.HexColor("#9d174d")
RED_BG   = colors.HexColor("#fdf2f8")
LINE     = colors.HexColor("#e5e7eb")
GREENBG  = colors.HexColor("#ecfdf5")

def brl(v):
    s = f"{v:,.0f}".replace(",", ".")
    return f"R$ {s}"

styles = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=styles["Title"], fontName="Helvetica-Bold",
                    fontSize=22, textColor=INK, spaceAfter=2, alignment=TA_CENTER)
SUB = ParagraphStyle("SUB", parent=styles["Normal"], fontSize=11, textColor=GOLD,
                     alignment=TA_CENTER, spaceAfter=2, fontName="Helvetica-Bold")
SMALLC = ParagraphStyle("SMALLC", parent=styles["Normal"], fontSize=8.5, textColor=MUTED,
                        alignment=TA_CENTER)
H2 = ParagraphStyle("H2", parent=styles["Heading2"], fontName="Helvetica-Bold",
                    fontSize=13, textColor=INK, spaceBefore=10, spaceAfter=6)
BODY = ParagraphStyle("BODY", parent=styles["Normal"], fontSize=10, textColor=INK,
                      leading=14, spaceAfter=4)
NOTE = ParagraphStyle("NOTE", parent=styles["Normal"], fontSize=8.5, textColor=MUTED,
                      leading=11)
CARDTITLE = ParagraphStyle("CARDTITLE", parent=styles["Normal"], fontName="Helvetica-Bold",
                           fontSize=12, textColor=colors.white)
CARDSUB = ParagraphStyle("CARDSUB", parent=styles["Normal"], fontSize=8.5, textColor=colors.white)
CELL = ParagraphStyle("CELL", parent=styles["Normal"], fontSize=9, textColor=INK, leading=12)
CELLB = ParagraphStyle("CELLB", parent=styles["Normal"], fontSize=9, textColor=INK,
                       leading=12, fontName="Helvetica-Bold")
CELLR = ParagraphStyle("CELLR", parent=CELL, alignment=2)
CELLRB = ParagraphStyle("CELLRB", parent=CELLB, alignment=2)
TAG = ParagraphStyle("TAG", parent=styles["Normal"], fontSize=8, textColor=colors.white,
                     fontName="Helvetica-Bold")

doc = SimpleDocTemplate(OUT, pagesize=A4,
                        leftMargin=18*mm, rightMargin=18*mm,
                        topMargin=16*mm, bottomMargin=14*mm)
S = []

# ===== Cabecalho =====
S.append(Paragraph("Proposta de Viagem &mdash; China", H1))
S.append(Paragraph("Pequim &bull; Harbin", SUB))
S.append(Paragraph("Inverno 2026 &nbsp;|&nbsp; 30/nov a 14/dez", SMALLC))
S.append(Spacer(1, 8))
S.append(HRFlowable(width="100%", thickness=1, color=LINE))
S.append(Spacer(1, 8))

intro = ("Plano de viagem para <b>Pequim e Harbin</b>, na China. Os voos internacionais "
         "(ida e volta Belo Horizonte&ndash;Pequim) tem datas fixas; o trecho de trem "
         "Pequim&ndash;Harbin (ida e volta) fica definido depois, dentro da janela da viagem. "
         "Viagem para <b>3 pessoas</b>. Abaixo, as <b>duas opcoes de passagem</b> "
         "que selecionamos, com o custo completo <b>por pessoa</b> (valor individual &mdash; cada um paga o seu).")
S.append(Paragraph(intro, BODY))
S.append(Spacer(1, 6))

# ===== Datas =====
datas = [
    [Paragraph("<b>Ida</b>", CELLB), Paragraph("30/nov/2026 &mdash; chegada em Pequim 02/dez", CELL)],
    [Paragraph("<b>Volta</b>", CELLB), Paragraph("13/dez/2026 &mdash; chegada em BH 14/dez", CELL)],
    [Paragraph("<b>Harbin</b>", CELLB), Paragraph("Trem Pequim&harr;Harbin &mdash; datas a definir (dentro da viagem)", CELL)],
]
t = Table(datas, colWidths=[24*mm, 150*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#f9fafb")),
    ("BOX", (0,0), (-1,-1), 0.5, LINE),
    ("INNERGRID", (0,0), (-1,-1), 0.5, LINE),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
]))
S.append(t)
S.append(Spacer(1, 12))

# ===== Funcao card de opcao =====
COMMON = [
    ("Hospedagem (Pequim + Harbin)", 700),
    ("Internet / eSIM", 250),
    ("Alimentacao", 1000),
    ("Trem Pequim &harr; Harbin (ida + volta)", 843),
    ("Extras (atracoes, transporte, ingressos)", 500),
]

def option_card(tag, tagcolor, title, subtitle, flight_rows, flight_price, total_pp, accentbg):
    # faixa de titulo
    head = Table([[Paragraph(title, CARDTITLE)],
                  [Paragraph(subtitle, CARDSUB)]], colWidths=[174*mm])
    head.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), tagcolor),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (0,0), 7), ("BOTTOMPADDING", (0,1), (-1,1), 7),
        ("TOPPADDING", (0,1), (-1,1), 0),
    ]))

    rows = [[Paragraph("<b>Item</b>", CELLB), Paragraph("<b>Valor (por pessoa)</b>", CELLRB)]]
    # voo
    rows.append([Paragraph("<b>Passagem aerea</b> &mdash; ida e volta<br/>"
                           + "<font size=8 color='#6b7280'>" + flight_rows + "</font>", CELL),
                 Paragraph("<b>"+brl(flight_price)+"</b>", CELLRB)])
    for label, val in COMMON:
        rows.append([Paragraph(label, CELL), Paragraph(brl(val), CELLR)])
    rows.append([Paragraph("<b>TOTAL POR PESSOA</b>", CELLB),
                 Paragraph("<b>"+brl(total_pp)+"</b>", CELLRB)])

    body = Table(rows, colWidths=[128*mm, 46*mm])
    body.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#f3f4f6")),
        ("BACKGROUND", (0,-1), (-1,-1), accentbg),
        ("BOX", (0,0), (-1,-1), 0.5, LINE),
        ("INNERGRID", (0,0), (-1,-1), 0.4, LINE),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("LINEABOVE", (0,-1), (-1,-1), 1, tagcolor),
    ]))
    wrap = Table([[head],[body]], colWidths=[174*mm])
    wrap.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 1, tagcolor),
        ("TOPPADDING", (0,0), (-1,-1), 0), ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ]))
    return wrap

S.append(Paragraph("Opcoes de passagem", H2))

# Opcao A - Qatar via Doha
A_flight = ("LATAM + Qatar Airways &bull; via Sao Paulo (GRU) + Doha (DOH)<br/>"
            "Ida 30/nov 19:55 &rarr; 14:45 (+2) &bull; Volta 13/dez 18:15 &rarr; 14:30 (+1)<br/>"
            "Bagagem: 1 de mao + <b>2 despachadas gratis</b>")
S.append(KeepTogether(option_card("MAIS BARATA", GOLD,
                      "Opcao A &mdash; Qatar via Doha  (mais barata)",
                      "Melhor preco em dinheiro &bull; 2 malas despachadas gratis",
                      A_flight, 8766, 12059, GOLD_BG)))
S.append(Spacer(1, 10))

# Opcao B - LATAM via Frankfurt
B_flight = ("LATAM + Air China &bull; via Sao Paulo (GRU) + Frankfurt (FRA)<br/>"
            "Ida 30/nov 18:00 &rarr; 11:25 (+2) &bull; Volta 13/dez 14:30 &rarr; 09:30 (+1)<br/>"
            "Tarifa Standard com mala despachada inclusa &bull; <b>permite compra com milhas</b>")
S.append(KeepTogether(option_card("LATAM / MILHAS", RED,
                      "Opcao B &mdash; LATAM via Frankfurt  (milhas)",
                      "Compra direta na LATAM &bull; mala inclusa &bull; aceita milhas LATAM Pass",
                      B_flight, 9457, 12750, RED_BG)))
S.append(Spacer(1, 12))

# ===== Resumo comparativo =====
S.append(Paragraph("Resumo &mdash; valor individual (por pessoa)", H2))
comp = [
    [Paragraph("<font color='white'><b>Opcao</b></font>", CELL),
     Paragraph("<font color='white'><b>Passagem</b></font>", CELLR),
     Paragraph("<font color='white'><b>Demais custos</b></font>", CELLR),
     Paragraph("<font color='white'><b>Total por pessoa</b></font>", CELLR)],
    [Paragraph("A &mdash; Qatar via Doha", CELL), Paragraph(brl(8766), CELLR),
     Paragraph(brl(3293), CELLR), Paragraph("<b>"+brl(12059)+"</b>", CELLRB)],
    [Paragraph("B &mdash; LATAM via Frankfurt", CELL), Paragraph(brl(9457), CELLR),
     Paragraph(brl(3293), CELLR), Paragraph("<b>"+brl(12750)+"</b>", CELLRB)],
]
tc = Table(comp, colWidths=[64*mm, 34*mm, 38*mm, 38*mm])
tc.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), INK),
    ("BOX", (0,0), (-1,-1), 0.5, LINE),
    ("INNERGRID", (0,0), (-1,-1), 0.4, LINE),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("BACKGROUND", (0,1), (-1,1), GOLD_BG),
    ("BACKGROUND", (0,2), (-1,2), RED_BG),
]))
S.append(tc)
S.append(Paragraph("Viagem para <b>3 pessoas</b> &mdash; os valores acima sao <b>por pessoa</b> "
                   "(valor individual; cada um paga o seu).", NOTE))
S.append(Spacer(1, 12))

# ===== Aprovacao / proximos passos =====
S.append(Paragraph("Como funciona a aprovacao", H2))
steps = ("<b>1.</b> Aprovado o <b>preco</b> de uma das opcoes acima.&nbsp; "
         "<b>2.</b> Eu compro as passagens (Opcao B na LATAM se formos de milhas).&nbsp; "
         "<b>3.</b> Com os voos garantidos, decidimos juntos as <b>datas de Harbin</b> "
         "(festival de gelo, roupa de frio) e o restante do roteiro.")
box = Table([[Paragraph(steps, BODY)]], colWidths=[174*mm])
box.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), GREENBG),
    ("BOX", (0,0), (-1,-1), 0.5, colors.HexColor("#a7f3d0")),
    ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
]))
S.append(box)
S.append(Spacer(1, 10))

# ===== Notas =====
S.append(HRFlowable(width="100%", thickness=0.5, color=LINE))
S.append(Spacer(1, 4))
notas = (
    "<b>Observacoes:</b> valores por pessoa, em reais. Precos de passagem aerea mudam o tempo todo &mdash; "
    "os valores acima sao referencia da pesquisa atual. &bull; Hospedagem e extras sao estimativas conservadoras, "
    "a refinar conforme escolha de hoteis e atracoes. &bull; Harbin em dezembro chega a -20&deg;C/-30&deg;C: prever roupa de frio. &bull; "
    "China bloqueia Google/WhatsApp/Instagram &mdash; levar eSIM/VPN configurado antes. &bull; "
    "Para usar milhas, a compra precisa ser feita direto no site da LATAM (OTAs como Expedia nao aceitam resgate)."
)
S.append(Paragraph(notas, NOTE))
S.append(Spacer(1, 6))
links = ("<b>Links das passagens (Google Voos):</b><br/>"
         "Opcao A (Qatar/Doha): https://www.google.com/travel/flights/s/vHg3PcdZvG7kZwjr9<br/>"
         "Opcao B (LATAM/Frankfurt): https://www.google.com/travel/flights/s/kzvNkgKrtdD3FVSd7")
S.append(Paragraph(links, NOTE))

doc.build(S)
print("OK ->", OUT)
