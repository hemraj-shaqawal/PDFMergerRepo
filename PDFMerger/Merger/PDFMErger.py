import  logging as logger
import  os
import PyPDF2

logger.basicConfig(filename="appLog.log",level= logger.INFO,format="%(asctime)s %(levelname)s %(message)s")

class PdfMerger:

    def __init__(self,path):
        """Please provide a path where you want to merge all files"""
        if os.path.exists(path):
            self.path = path;
        else:
            raise Exception("This path is invalid!, try again!")


    def getAllPDFFile(self):
        filename = os.listdir(self.path)
        pdf_file_list = [item for item in filename if ".pdf" in item]
        if len(pdf_file_list) > 0:
            return pdf_file_list
        else:
            return []
            # "PDF file is not exists in this path "+self.path

    def mergeAllPDFFile(self,outputFile):
        # creating pdf file merger object
        pdfMerger = PyPDF2.PdfFileMerger()

        try:
            filename = self.getAllPDFFile()

            for item in filename:
                pathoffile = self.path+"\\"+item
                pdfMerger.append(pathoffile)

                with open(outputFile,"wb") as f:
                    pdfMerger.write(f)
                
            return "Your PDF file has been created with name of " + outputFile

        except Exception as e:
                logger.exception("Error occurd =" + str(e))
