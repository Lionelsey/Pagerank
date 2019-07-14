import xlsxwriter
f2 = open("WikiData.txt")
l1=[]
workbook = xlsxwriter.Workbook("text.xlsx")
worksheet = workbook.add_worksheet()
j=1
for line in open('optimize_result.txt'):
    data = line.partition(" ")
    x = int(data[0])
    y = float(data[2])
    l1.append(x)
    worksheet.write(0, j, x)
    worksheet.write(j, 0, x)
    worksheet.write(j, j, 505-j*5)
    for i in range(j-1):
        worksheet.write(j, i+1, 0)
    j+=1
for line in open("WikiData.txt"):
    data = line.partition("	")
    x = int(data[0])
    y = int(data[2])
    if(l1.count(x)+l1.count(y)==2):
        if(l1.index(x)>l1.index(y)):
            worksheet.write(l1.index(x)+1, l1.index(y)+1, 35)
        else:
            worksheet.write(l1.index(y) + 1, l1.index(x) + 1, 35)
workbook.close()
