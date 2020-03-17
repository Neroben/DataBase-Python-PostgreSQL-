import psycopg2

def init():
    return psycopg2.connect(
        database="postgres",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432")

#curr = con.cursor()

#curr.execute("""
#INSERT INTO confederacy(name)
#VALUES('Золотая лига');
#""")
#con.commit()

#curr.execute("""
#SELECT DISTINCT SP.name
#from sponsor SP, (  SELECT DISTINCT CL.club_id, CL.sponsor_id
#                    FROM club CL, confederacy CO, ( SELECT CL.club_id, count(MC)
#                                                    FROM club CL, ( SELECT CL.club_id, MC.playdata
#                                                                    FROM match MC, club CL
#                                                                    WHERE CL.club_id = MC.club_id1 or CL.club_id = MC.club_id2) MC
#                                                    where CL.club_id = MC.club_id
#                                                    group by CL.club_id) MC2
#                    where Cl.rating > 10 and CL.confederacy_id = 1 and MC2.club_id = CL.club_id and MC2.count < 5) CL2
#where SP.name LIKE('%Б%') and SP.sponsor_id = CL2.sponsor_id;
#""")


#result = curr.fetchone()
#reader_name = result[0]

#print(reader_name)

# Закрываем подключение
#curr.close()
#con.close()
