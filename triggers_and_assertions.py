import sqlite3
import datetime

if __name__ == "__main__":
    present = datetime.datetime.today().strftime("%Y-%m-%d")
    db = sqlite3.connect("pharmacy.sqlite")

    db.execute("CREATE TRIGGER exp_check BEFORE UPDATE ON  stocks " +
               "BEGIN " +
               " SELECT " +
               "CASE " +
               " WHEN NEW.expdate <= " + present + " OR NEW.expdate < OLD.expdate THEN " +
               " RAISE (ABORT, 'Invalid Expiry Date') " +
               "END;" +
               " END;")

    db.execute("CREATE TRIGGER qty_check BEFORE UPDATE ON  stocks " +
               "BEGIN " +
               " SELECT " +
               "CASE " +
               " WHEN NEW.qty < 0 THEN " +
               " RAISE (ABORT, 'Invalid Expiry Date') " +
               "END;" +
               " END;")

    # Creating Assertions
    # db.execute("CREATE ASSERTION exp_date_check CHECK (" +
    #            "SELECT expdate FROM stocks WHERE expdate < " + present + " );")
    #
    # db.execute("CREATE ASSERTION profit_check CHECK (" +
    #            "SELECT sid FROM stocks WHERE (cust_unit_price - dist_unit_price) <= 0);")

    # Correlated qeury
    print(db.execute("SELECT tablets.mname, stocks.qty, stocks.cust_unit_price, stocks.expdate " +
                     "FROM tablets, stocks WHERE" +
                     " tablets.mid = stocks.tid AND stocks.cust_unit_price >= " +
                     "(SELECT AVG(cust_unit_price) FROM stocks);"))
