from BeautifulSoup import BeautifulStoneSoup
import urllib2

from datetime import datetime

class BodisApi:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_domains(self):
        url = "https://api.bodis.com/domains?apikey=%s&count=30000" % self.api_key

        data = urllib2.urlopen(url).read()

        soup = BeautifulStoneSoup(data)
        domain_list = []
        results = soup.results
        for result in results.findAll('result'):
            domainname = result.domainname
            data = {'name': domainname.contents[0].encode('utf-8')}

            domain_list.append(data)

        return domain_list

    def report_domain(self, domain_name, start_date="28/01/2013"):

        url = "https://api.bodis.com/reporting?apikey=%s&domain=%s&BreakDownBy=Day&Count=10000&StartDate=%s" % (self.api_key, domain_name, start_date)
        data = urllib2.urlopen(url).read()

        soup = BeautifulStoneSoup(data)
        results = soup.results

        r = []
        for result in results.findAll('result'):
            datum = "%s.%s.%s" % (result.day.string, result.month.string, result.year.string)
            datum = datetime.strptime(datum, '%d.%m.%Y')
            r.append({
                'datum': datum,
                'visitors': int(result.visitors.string),
                'clicks': int(result.clicks.string),
                'revenue': float(result.revenue.string)})

        return r

    def domain_revenue(self, domain_name):
        url = "https://api.bodis.com/reporting?apikey=%s&domain=%s&BreakDownBy=DomainName" % (self.api_key, domain_name)

        data = urllib2.urlopen(url).read()

        soup = BeautifulStoneSoup(data)
        result = soup.result

        """
        r = []
        for result in results.findAll('result'):
            datum = "%s.%s.%s" % (result.day.string, result.month.string, result.year.string)
            datum = datetime.strptime(datum, '%d.%m.%Y')
            r.append({
                'datum': datum,
                'visitors': int(result.visitors.string),
                'clicks': int(result.clicks.string),
                'revenue': float(result.revenue.string)})
        """
        if not result:
            return {}
        r = {}
        for k in ('visitors', 'clicks', 'ctr', 'cpc', 'rpm', 'revenue'):
            r[k] = result.find(k).string



        return r


    def add_domain(self, domain_name):
        """Add Domain to Bodis.

        :param domain_name: Domain Name
        :type domain_name: str
        """
        url = "https://api.bodis.com/addDomains?apikey=%s&domain1=%s" % (self.api_key, domain_name)
        data = urllib2.urlopen(url).read()
        print data

        return True

    def delete_domain(self, domain_name):
        """Delete domain from Bodis account.

        :param domain_name: Domain Name
        :type domain_name: str
        """
        url = "https://api.bodis.com/deleteDomains?apikey=%s&domain1=%s" % (self.api_key, domain_name)
        data = urllib2.urlopen(url).read()
        print data

        return True

    def country_reporting(self, domain_name):

        url ="https://api.bodis.com/countryreporting?apikey=%s&domain=%s&format=json" % (self.api_key, domain_name)

        data = urllib2.urlopen(url).read()

        return data

    def referrer_reporting(self, domain_name):

        url = "https://api.bodis.com/referrersitereporting?apikey=%s&domain=%s&format=json" % (self.api_key, domain_name)

        data = urllib2.urlopen(url).read()

        return data

    def domains(self):

        url = "https://api.bodis.com/domains?apikey=%s&orderBy=DatetimeAdded&orderType=desc&Count=10000&format=json" % (self.api_key)

        data = urllib2.urlopen(url).read()

        return data





