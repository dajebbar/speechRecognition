from pdfminer.high_level import extract_text


def get_text(pth):
    # Check extension of file
    if pth[pth.index('.')+1:] != "pdf":
        assert "file must be pdf extension"
    # extract file
    text = extract_text(pth)
    # write text in new file.txt
    with open(f"{pth[:pth.index('.')]}.txt", "a") as f:
        f.write(text)
    print("file is ready to translate!")
    return 

if __name__=="__main__":
    # pth = "pdf_extracter/Data Scientist senior.docx"
    pth = "ChoosingAWinningNiche.pdf"

    get_text(pth)