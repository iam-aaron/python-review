
text = "X-DSPAM-Confidence:    0.8475"
str = text[text.find(":")+1:].lstrip()
print(float(str))
