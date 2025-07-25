from fpdf import FPDF
import pandas as pd 

df=pd.read_csv("data/topics.csv")
pdf=FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
for index,row in df.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page()

        pdf.set_font(family="Times",style="B",size=24)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10,21,200,21)
        pdf.ln(258)
        pdf.set_font(family="Times",style="B",size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=0,txt=row["Topic"],align="R")


pdf.output("output.pdf")