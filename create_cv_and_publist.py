import os, glob

CMD = "pdflatex -synctex=1 -interaction=nonstopmode {fname}.tex"

for tag in ["Vijaykumar_CV", "Vijaykumar_CV_with_pubs", "Vijaykumar_pubs"]:
	for filename in glob.glob(tag + "*"):
		if not filename.endswith(".tex"):
			os.remove(filename)

	os.system(CMD.format(fname=tag))
	os.system(CMD.format(fname=tag))

	for filename in glob.glob(tag + "*"):
		if filename.endswith(".pdf") or filename.endswith(".tex"):
			continue
		os.remove(filename)
