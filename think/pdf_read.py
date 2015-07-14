import optparse
import pyPdf


def print_meta(fn):
    pdf = pyPdf.PdfFileReader(open(fn,'rb'))
    doc_info = pdf.getDocumentInfo()
    print('[*] PDF MetaData For: %s' % str(fn))
    for meta_item in doc_info:
        print('[+] %s: %s' % (meta_item, doc_info[meta_item]))



fn = 'ANONOPS_The_Press_Release.pdf'
print_meta(fn)




# parser = optparse.OptionParser('usage%prog -F <PDF file name>')
# parser.add_option('-F', dest='fn', type='string', help='specify PDF file name')
# (options, args) = parser.parse_args()
# fn = options.fn
# if not fn:
    # print(parser.usage)
    # exit(0)
