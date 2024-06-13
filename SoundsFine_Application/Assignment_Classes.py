class Genre:

    def __init__(self, genreName):
        self.__genreName = genreName

    def readGenreName(self):
        return self.__genreName

    def updateGenreName(self, newGenreName):
        self.__genreName = newGenreName


class Singer(Genre):

    # Inheritance
    def __init__(self, singerName, singerNationality, priceConcert, availableConcert, genreName, time, local,
                 ticketSeatingCode):
        super().__init__(genreName)

        self.__singerNationality = singerNationality
        self.__singerName = singerName
        self.__priceConcert = priceConcert
        self.__availableConcert = availableConcert

        # aggregation
        self.__concert = Concert(time, local, ticketSeatingCode)

    def readSingerName(self):
        return self.__singerName

    def readSingerNationality(self):
        return self.__singerNationality

    def readPriceConcert(self):
        return self.__priceConcert

    def updatePriceConcert(self, newPriceConcert):
        self.__priceConcert = newPriceConcert

    def readAvailableConcert(self):
        return self.__availableConcert

    def readGenreName(self):
        return Genre.readGenreName(self)

    def readDetails1(self):
        return 'Genre: ' + str(self.readGenreName()) + ' / ' + ' Singer: ' + str(self.readSingerName())

    def readDetails2(self):
        return 'Time: ' + str(self.__concert.readTime()) + ' / ' + ' Local: ' + str(self.__concert.readLocal())

    def readDetails3(self):
        return 'Seating Number / Ticket Code: ' + str(self.__concert.readTicketSeatingCode())

    # Polymorphism Methods in the Jazz, Country, Pop, Rock subclasses
    def readSongName(self):
        return ''

    def readSongTrackTime(self):
        return ''


class Jazz(Singer):

    # Inheritance
    def __init__(self, songName, songTrackTime, singerName, singerNationality, priceConcert, availableConcert,
                 genreName, time, local, ticketSeatingCode):
        super().__init__(singerName, singerNationality, priceConcert, availableConcert, genreName, time, local,
                         ticketSeatingCode)

        self.__songName = songName
        self.__songTrackTime = songTrackTime

    # Polymorphism Methods
    def readSongName(self):
        return self.__songName

    def readSongTrackTime(self):
        return self.__songTrackTime


class Country(Singer):

    # Inheritance
    def __init__(self, songName, songTrackTime, singerName, singerNationality, priceConcert, availableConcert,
                 genreName, time, local,
                 ticketSeatingCode):
        super().__init__(singerName, singerNationality, priceConcert, availableConcert, genreName, time, local,
                         ticketSeatingCode)

        self.__songName = songName
        self.__songTrackTime = songTrackTime

    # Polymorphism Methods
    def readSongName(self):
        return self.__songName

    def readSongTrackTime(self):
        return self.__songTrackTime


class Pop(Singer):

    # Inheritance
    def __init__(self, songName, songTrackTime, singerName, singerNationality, priceConcert, availableConcert,
                 genreName, time, local,
                 ticketSeatingCode):
        super().__init__(singerName, singerNationality, priceConcert, availableConcert, genreName, time, local,
                         ticketSeatingCode)

        self.__songName = songName
        self.__songTrackTime = songTrackTime

    # Polymorphism Methods
    def readSongName(self):
        return self.__songName

    def readSongTrackTime(self):
        return self.__songTrackTime


class Rock(Singer):

    # Inheritance
    def __init__(self, songName, songTrackTime, singerName, singerNationality, priceConcert, availableConcert,
                 genreName, time, local,
                 ticketSeatingCode):
        super().__init__(singerName, singerNationality, priceConcert, availableConcert, genreName, time, local,
                         ticketSeatingCode)

        self.__songName = songName
        self.__songTrackTime = songTrackTime

    # Polymorphism Methods
    def readSongName(self):
        return self.__songName

    def readSongTrackTime(self):
        return self.__songTrackTime


class Concert():

    def __init__(self, time, local, ticketSeatingCode):
        # private variables
        self.__time = time
        self.__local = local
        self.__ticketSeatingCode = ticketSeatingCode

    def readTime(self):
        return self.__time

    def readLocal(self):
        return self.__local

    def readTicketSeatingCode(self):
        return self.__ticketSeatingCode
