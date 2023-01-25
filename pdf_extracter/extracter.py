from pdfminer.high_level import extract_text


def get_text(pth):
    # Check extension of file
    if pth[".":] != "pdf":
        assert "file must be pdf extension"
    # extract file
    text = extract_text(pth)
    # write text in new file.txt
    with open(f"{pth[:'.']}.txt", "a") as f:
        f.write(text)

    return "file is ready to translate!"

if __name__=="__main__":
    pth = "./pdf_extracter/Data Scientist senior.docx"

    get_text(pth)