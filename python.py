import matplotlib.pyplot as p

circle = [35, 22, 16, 12, 10, 7]
langs = ["python", "java", "java script", "html", "css", "json"]

p.pie(circle, labels=langs)
p.show()
