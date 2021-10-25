from database.db import engine


def create_new_employee(employee_json: dict):
    name = employee_json['name']
    if employee_already_registered(employee_json['rfc']):
        print(f'Bienvenide de vuelta, {name}!')
    query = f'''
                 insert into employee
                 (id,
                  rfc, 
                  name,
                  last_name,
                  start_date,
                  birthday,
                  job_position,
                  pronouns
                  ) 
                 values 
                 (
                    '{employee_json['id']}', 
                    '{employee_json['rfc']}',
                    '{name}'
                    '{employee_json['last_name']}',
                    '{employee_json['start_day']}',
                    '{employee_json['birthday']}',
                    '{employee_json['job_position']}',
                    '{employee_json['pronouns']}',
                 )       
                 '''
    with engine.connect() as conn:
        conn.execute(query)


def employee_already_registered(rfc):
    query = f"select count(*) from chronos_user where rfc='{rfc}'"
    count = execute_db_query(query)
    return count[0][0] == 1


def execute_db_query(query):
    with engine.connect() as conn:
        results = conn.execute(query).fetchall()

    return results
