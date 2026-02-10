------- import dos dados: extract
with source as(
    select
        "jobTitle", 
        "companyName", 
        "jobType",
        "jobGeo",
        "jobLevel",
        "annualSalaryMin",
        "annualSalaryMax",
        "salaryCurrency"
    from {{source('SEGUROS', 'listagem_trabalhos_remoto')}}
),
------ renamed: inserir transformações
renamed as (
    select
        "jobTitle" as titulo_vaga, 
        "companyName" as nome_empresa, 
        "jobType" as tipo_trabalho,
        "jobGeo" as localizacao,
        "jobLevel" as senioridade,
        cast(nullif("annualSalaryMin", '') as float) as minimo_salario_anual,
        cast(nullif("annualSalaryMax", '') as float) as maximo_salario_anual,
        "salaryCurrency" as moeda
    from source
),
---- final: select final
final as (
    select 
        titulo_vaga,
        nome_empresa,
        tipo_trabalho,
        localizacao,
        senioridade,
        minimo_salario_anual/12 as minimo_salario_mensal,
        minimo_salario_anual,
        maximo_salario_anual/12 as maximo_salario_mensal,
        maximo_salario_anual,
        moeda
    from renamed
)

select * from final