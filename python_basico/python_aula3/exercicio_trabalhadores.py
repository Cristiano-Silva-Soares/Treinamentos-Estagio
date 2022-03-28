import psycopg2

def call_dt():

    try:
        connection = psycopg2.connect(
            host='127.0.0.1',
            database='Employees',
            user='postgres',
            password=123456
        )
        print('Conexão feita!')

        cursor = connection.cursor()
        cursor.execute('insert * from Employees')
        cursor.commit()

        cursor.execute('select * from Employees')
        result = cursor.fetchall()
        print(result)

        cursor.close()
        connection.close()

    except Exception:
        print('Falha na conexão!')


for n in range(2):

    name = str(input('Entre com o nome do funcionário: '))
    gender = str(input('Entre com o sexo do funcionário: '))
    salary = float(input('Entre com o salário do funcionário: '))

    call_dt()


