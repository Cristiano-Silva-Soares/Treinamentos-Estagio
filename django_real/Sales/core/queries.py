from core import models
from django.db.models import Value, Case, When, CharField, Q, F, FloatField, ExpressionWrapper, Exists, OuterRef
from django.db.models.functions import Extract, Now


# 1) Fazer uma consulta para retornar todos os funcionários que contenham silva no nome;
def questao1():
    qs = models.Employee.objects.filter(name__icontains='silva')
    return qs


# 2) Fazer uma consulta para retornar todos os funcionários com o salário maior que R$ 5.000;
def questao2():
    qs = models.Employee.objects.filter(salary__gt=5000)
    return qs


# 3) Fazer uma consulta para trazer todos os clientes que tem uma renda mensal inferior a R$ 2.000,00;
def questao3():
    qs = models.Customer.objects.filter(income__lt=2000)
    return qs


# 4) Fazer uma consulta para retornar todos os funcionários admitidos entre 2010 e 2021.
def questao4():
    qs = models.Employee.objects.filter(admission_date__range=['2010-01-01', '2021-12-31'])
    return qs


# - 5) Fazer uma consulta para retornar todos os funcionários casados ou solteiros;
def questao5():
    qs = models.Employee.objects.filter(Q(marital_status=1) | Q(marital_status=2)).values('id', 'name',
                                                                                          'marital_status')
    return qs


# -- 6) Fazer uma consulta para retornar todos os funcionários que ganham entre R$ 1.000,00 e R$ 5.000,00;
def questao6():
    qs = models.Employee.objects.filter(salary__gte=1000).filter(salary__lt=5000).values('id', 'name', 'salary')
    return qs


# -- 7) Fazer uma consulta que retorne a diferença do preço de custo e preço de venda dos produtos;
def questao7():
    qs = models.Product.objects.annotate(calcula_diferenca=ExpressionWrapper(F('sale_price') - F('cost_price'),
                                                                             output_field=FloatField())).values(
        'calcula_diferenca')
    return qs


# - 8) Fazer uma consulta para retornar todos os funcionários que não tenham salário entre R$ 4.000,00 e R$ 8.000,00;
def questao8():
    qs = models.Employee.objects.exclude(salary__range=[4000, 8000]).values('id', 'name', 'salary')
    return qs


# 9) Fazer uma consulta para retornar todos os clientes que já tenham alguma venda, não pode usar JOIN;
def questao9():
    sub_qs = models.Sale.objects.filter(id_custumer=OuterRef('id'))
    qs = models.Customer.objects.annotate(sale_customer=Exists(sub_qs)).filter(sale_customer=True).values('name')
    return qs


# 10) Fazer uma consulta para retornar todos os funcionários que já tenham alguma venda, não pode usar JOINdef questao10():
def questao10():
    sub_qs = models.Sale.objects.filter(employee_id=OuterRef('id'))
    qs = models.Employee.objects.annotate(sale_employee=Exists(sub_qs)).filter(sale_employee=True).values('name')
    return qs


# 11) Fazer uma consulta retornar para retornar as vendas entre 2010 e 2021
def questao11():
    qs = models.Sale.objects.filter(date__range=['2010-01-01', '2021-12-31'])
    return qs


# 12) Fazer uma consulta para retornar o nome do funcionario e o sexo de forma descritiva
def questao12():
    qs = models.Employee.objects.annotate(
        gender_qs=Case(When(gender=models.Employee.Gender.FEMALE), then=Value('FEMALE'), default=Value('MALE'),
                       OutputField=CharField())).values('id', 'name', 'gender_qs')
    return qs

# 13) Fazer uma consulta para retornar um status para o funcionário de acordo com a sua idade.
#       * 18 - 25, Jr.
#       * 26 - 34, Pleno.
#       * 35 ou mais, Sênior.
# def questao13():
#     qs = models.Employee.objects.annotate(get_age=Extract(ExpressionWrapper(Value(Now()-F))))
