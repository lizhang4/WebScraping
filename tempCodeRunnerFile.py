for t in soup.find_all('div') :
    if (len(t.getText()) > 30):
        print(t.text)