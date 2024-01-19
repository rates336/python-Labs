
class HtmlCM:

    def __init__(self):
        pass

    def __enter__(self):
        print('''<TABLE>
 <TR>
     <TH>Number</TH><TH>Description</TH>
 </TR>''')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('</TABLE>')


with HtmlCM() as h:
    print(" <TR>")
    print("     <TD>1</TD><TD>Say hello!</TD)")
    print(" </TR>")
    print(" <TR>")
    print("     <TD>2</TD><TD>Say good bye!</TD)")
    print(" </TR>")