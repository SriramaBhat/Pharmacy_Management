import sqlite3

if __name__ == "__main__":
    db = sqlite3.connect("pharmacy.sqlite")
    db.execute("CREATE TABLE IF NOT EXISTS employee ( eid INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "ename VARCHAR(50) NOT NULL, ephone VARCHAR(12) NOT NULL, edob DATE NOT NULL, " +
               "egender VARCHAR(25) NOT NULL, eaddress TEXT NOT NULL, eemail VARCHAR(255) NOT NULL, " +
               "epassword VARCHAR(255) NOT NULL);")

    db.execute("CREATE TABLE IF NOT EXISTS admin ( aid INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "aname VARCHAR(50) NOT NULL, aphone VARCHAR(12) NOT NULL, " +
               "adob DATE NOT NULL, " + "agender VARCHAR(25) NOT NULL, " +
               "aaddress TEXT NOT NULL, aemail VARCHAR(255) NOT NULL, " +
               "apassword VARCHAR(255) NOT NULL);")

    db.execute("INSERT INTO employee (ename, ephone, edob, egender, eaddress, eemail, epassword) VALUES " +
               "('Test Employee 1', '4656543457', '2002-12-14', 'Male', '414, Vidyashankar Layout," +
               " Shakthi Nagar, Satagalli, Mysuru', 'test1@test.com', 'helloworld123#' );")

    db.execute("INSERT INTO admin (aname, aphone, adob, agender, aaddress, aemail, apassword) VALUES" +
               "('Srirama Bhat', '9148466270', '2002-11-14', 'Male', '412, HPO & RMS Layout, Shaktinagar, Satagalli, " +
               "Mysuru', 'sriramabhat14@gmail.com', 'helloworld123$');")

    db.execute("CREATE TABLE IF NOT EXISTS tablets (mid INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "mname VARCHAR(255) NOT NULL, composition TEXT NOT NULL, symptoms TEXT NOT NULL, " +
               "side_effects TEXT);")

    db.execute("CREATE TABLE IF NOT EXISTS syrups (mid INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "mname VARCHAR(255) NOT NULL, composition TEXT NOT NULL, symptoms TEXT NOT NULL, " +
               "side_effects TEXT);")

    db.execute("CREATE TABLE IF NOT EXISTS stocks (sid INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "tid INTEGER, syid INTEGER, qty INTEGER NOT NULL, cust_unit_price DECIMAL(7, 2) NOT NULL, " +
               "dist_unit_price DECIMAL(7, 2) NOT NULL, expdate DATE NOT NULL, " +
               "FOREIGN KEY(tid) REFERENCES tablets(mid) ON DELETE CASCADE, " +
               "FOREIGN KEY(syid) REFERENCES syrups(mid) ON DELETE CASCADE);")

    db.execute("CREATE TABLE IF NOT EXISTS stransactions ( stid INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "sid INTEGER NOT NULL, strans_name VARCHAR(255) NOT NULL, tran_date DATE NOT NULL, " +
               "tran_time TIME NOT NULL, total_amt INTEGER NOT NULL);")

    db.execute("CREATE TABLE IF NOT EXISTS ctransactions ( ctid INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "cid INTEGER NOT NULL, ctrans_name VARCHAR(255) NOT NULL, tran_date DATE NOT NULL, " +
               "tran_time TIME NOT NULL, total_amt INTEGER NOT NULL);")

    db.execute("CREATE TABLE IF NOT EXISTS customers ( cust_id INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "cust_name VARCHAR(50) NOT NULL, " +
               "cust_email VARCHAR(255) NOT NULL, cust_symptoms TEXT NOT NULL);")

    db.execute("CREATE TABLE IF NOT EXISTS distributors ( dist_id INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "dist_name VARCHAR(50) NOT NULL, dist_phone VARCHAR(12) NOT NULL, dist_email VARCHAR(255) NOT NULL, " +
               "dist_address TEXT NOT NULL);")

    db.execute("COMMIT;")

    db.close()
