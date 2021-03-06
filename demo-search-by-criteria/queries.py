def select_reminders():
    query = f"""
    SELECT id, date, message 
    FROM `reminders` 
    ORDER by date ASC
    """
    return query

def select_by_searchword(searchword):
    query = f"""
    SELECT id, date, message, done 
    FROM `reminders` 
    WHERE message LIKE '%{searchword}%'
    ORDER by date ASC
    """
    return query

def insert_reminder(date, message):
    query = f"""
    INSERT INTO `reminders` (`date`, `message`, `done`) 
    VALUES ('{date}', '{message}', '0')
    """
    return query

def delete_reminder(reminder_id):
    query = f"""
    DELETE FROM `reminders`
    WHERE id = {reminder_id}
    """
    return query

def select_reminder(reminder_id):
    query = f"""
    SELECT date, message
    FROM `reminders`
    WHERE id = {reminder_id}
    """
    return query

def update_reminder(reminder_id, date, message):
    query = f"""
    UPDATE `reminders`
    SET date = '{date}', message = '{message}'
    WHERE id = {reminder_id}
    """
    return query

