class Candidate(object):
    def __init__(self, first_name=None, middle_name=None, last_name=None,
                 abbrev_name=None, suffix=None, use_suffix=False, 
                 ap_natl_number=None, ap_polra_number=None, ap_race_number=None,
                 combined_id=None, party=None, vote_total=None,
                 vote_total_percent=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.abbrev_name = abbrev_name
        self.suffix = suffix
        self.use_suffix = use_suffix
        self.ap_natl_number = ap_natl_number
        self.ap_polra_number = ap_polra_number
        self.ap_race_number = ap_race_number
        self.combined_id = combined_id
        self.party = party

    def __unicode__(self):
        if not self.last_name in ('Yes', 'No'):
            return u'%s %s' % (self.first_name, self.last_name)
        else:
            return u'%s' % self.last_name

    def __repr__(self):
        return u'<Candidate: %s>' % self.__unicode__()


class Race(object):
    def __init__(self, ap_number=None, office_name=None, office_descrip=None,
                 office_id=None, seat_name=None, seat_number=None, scope=None):
        self.ap_number = ap_number
        self.office_name = office_name
        self.office_descrip = office_descrip
        self.office_id = office_id
        self.seat_name = seat_name
        self.seat_number = seat_number
        self.scope = scope

    def get_name(self):
        name = ''
        if self.scope == 'L':
            if self.office_descrip:
                name = u'%s %s - %s' % (self.office_name, self.seat_name, self.office_descrip)
            else:
                name = u'%s %s' % (self.office_name, self.seat_name)
        else:
            if self.office_name == "Proposition":
                num = self.seat_name.split('-')[0].strip()
                name = "%s %s" % (self.office_name, num)
            else:
                name = u'%s' % self.office_name
        return name
    name = property(get_name)

    def __unicode__(self):
        return u'%s' % self.name

    def __repr__(self):
        return u'<Race: %s>' % self.__unicode__()
