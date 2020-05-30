from datetime import datetime
import datetime
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import csv
import json



#
def get_context(name,power,year):
    return {
        'name': 'mercedes',
        'power': 1.6,
        'year': 2016
    }
def from_template(name,power,year,template, signature):
    template = DocxTemplate(template)
    context = get_context(name,power,year)

    img_size = Cm(10)  # sets the size of the image
    logo = InlineImage(template, signature, img_size)

    context['logo'] = logo  # adds the InlineImage object to the context

    template.render(context)
    template.save('Auto' + '_' + str(datetime.datetime.now().date()) + 'report.docx')

def generate_report(name,power,year):
    template = 'temp.docx'
    signature = 'Logo.png'
    document = from_template(name,power,year,template, signature)



auto=[['name','power','year'],['mercedes','1.6','2016']]
with open('Auto.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(auto)

auto={'name':'mercedes', 'power':1.6, 'year':2016}


with open('auto.json','w') as f:
    (json.dump(auto,f))



if __name__== "__main__":
    import timeit
    print(timeit.timeit(generate_report()))



