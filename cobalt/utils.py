


def mechanize_fetch_cobalt_price_page():
    import mechanize
    br = mechanize.Browser()
    br.open('https://secure.lme.com/Data/Community/Login.aspx?ReturnUrl=%2fData%2fcommunity%2fDataprices_MM_OfficialPrices.aspx')
    br.select_form(nr=0)
    br['_logIn$_userID'] = 'jfmoxley'
    br['_logIn$_password'] = 'friesen'
    res = br.submit()
    content = res.read().decode('utf-8')
    return content


        
def main():
    mechanize_fetch_cobalt_price_page()

if __name__ == "__main__":
    main()
