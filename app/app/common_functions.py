def resultset(cursor):
    """"
        function for get all result set with key-value pair from table
    """
    sets = []
    while True:
        names = [c[0] for c in cursor.description]
        set_ = []
        while True:
            row_raw = cursor.fetchone()
            if row_raw is None:
                break
            row = dict(zip(names, row_raw))
            set_.append(row)
        sets.append(list(set_))
        if cursor.nextset() is None or cursor.description is None:
            break
    return sets