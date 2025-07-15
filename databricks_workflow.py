# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.49.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


Grupo01 = Job.from_dict(
    {
        "name": "Grupo01",
        "description": "# Grupo 01\n### Objetivo:\nWorkflow criado para executar a pipeline desde a coleta dos dados a partir de webscrapping e consumo de api's passando por todas as camadas de tratamento para consumo dos dashboard's",
        "email_notifications": {
            "no_alert_for_skipped_runs": True,
        },
        "webhook_notifications": {
            "on_success": [
                {
                    "id": "2d1ee673-9d65-438d-a60f-17fe842a4367",
                },
            ],
            "on_failure": [
                {
                    "id": "2d1ee673-9d65-438d-a60f-17fe842a4367",
                },
            ],
        },
        "notification_settings": {
            "no_alert_for_skipped_runs": True,
            "no_alert_for_canceled_runs": True,
        },
        "schedule": {
            "quartz_cron_expression": "22 0 7 * * ?",
            "timezone_id": "America/Sao_Paulo",
            "pause_status": "UNPAUSED",
        },
        "tasks": [
            {
                "task_key": "api_inpe",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/motores/api_inpe",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "bronze_chuvas_criticas",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/bronze/bronze_chuvas_criticas",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "GX_bronze_chuvas_criticas",
                "depends_on": [
                    {
                        "task_key": "bronze_chuvas_criticas",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/great_expectations/gx_bronze_chuvas_criticas",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "bronze_inpe",
                "depends_on": [
                    {
                        "task_key": "api_inpe",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/bronze/bronze_inpe",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "GX_bronze_INPE",
                "depends_on": [
                    {
                        "task_key": "bronze_inpe",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/great_expectations/gx_bronze_inpe",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "open_weather_map_api",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/motores/api_open_weather_map",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "bronze_open_weather_map",
                "depends_on": [
                    {
                        "task_key": "open_weather_map_api",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/bronze/bronze_open_weather_map",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "GX_bronze_open_weather_map",
                "depends_on": [
                    {
                        "task_key": "bronze_open_weather_map",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/great_expectations/gx_bronze_inpe",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "silver_chuvas_criticas",
                "depends_on": [
                    {
                        "task_key": "GX_bronze_chuvas_criticas",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/silver/silver_chuvas_criticas",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "GX_silver_chuvas_criticas",
                "depends_on": [
                    {
                        "task_key": "silver_chuvas_criticas",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/great_expectations/gx_silver_chuvas_criticas",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "silver_inpe",
                "depends_on": [
                    {
                        "task_key": "GX_bronze_INPE",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/silver/silver_inpe",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "GX_silver_INPE",
                "depends_on": [
                    {
                        "task_key": "silver_inpe",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/great_expectations/gx_silver_inpe",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "silver_open_weather_map_api",
                "depends_on": [
                    {
                        "task_key": "GX_bronze_open_weather_map",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/silver/silver_open_weather_map",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "GX_silver_open_weather_map",
                "depends_on": [
                    {
                        "task_key": "silver_open_weather_map_api",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/great_expectations/gx_silver_open_weather_map",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "weather_api",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/motores/api_weatherapi",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "bronze_weather_api",
                "depends_on": [
                    {
                        "task_key": "weather_api",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/bronze/bronze_weather_api",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "GX_bronze_weather_api",
                "depends_on": [
                    {
                        "task_key": "bronze_weather_api",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/great_expectations/gx_bronze_weather_api",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "silver_weather_api",
                "depends_on": [
                    {
                        "task_key": "GX_bronze_weather_api",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/silver/silver_weather_api",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "GX_silver_weather_api",
                "depends_on": [
                    {
                        "task_key": "silver_weather_api",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/great_expectations/gx_silver_weather_api",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "webscrapping_clima_tempo",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/motores/webscraping_clima_tempo",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "bronze_clima_tempo",
                "depends_on": [
                    {
                        "task_key": "webscrapping_clima_tempo",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/bronze/bronze_clima_tempo",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "GX_bronze_clima_tempo",
                "depends_on": [
                    {
                        "task_key": "bronze_clima_tempo",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/great_expectations/gx_bronze_weather_api",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "silver_clima_tempo",
                "depends_on": [
                    {
                        "task_key": "GX_bronze_clima_tempo",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/silver/silver_clima_tempo",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "GX_silver_clima_tempo",
                "depends_on": [
                    {
                        "task_key": "silver_clima_tempo",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/great_expectations/gx_silver_clima_tempo",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "webscrapping_weather",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/motores/webscraping_weather",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "bronze_weather",
                "depends_on": [
                    {
                        "task_key": "webscrapping_weather",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/bronze/bronze_weather",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "GX_bronze_weather",
                "depends_on": [
                    {
                        "task_key": "bronze_weather",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/great_expectations/gx_bronze_weather",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "silver_weather",
                "depends_on": [
                    {
                        "task_key": "GX_bronze_weather",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/silver/silver_weather",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "GX_silver_weather",
                "depends_on": [
                    {
                        "task_key": "silver_weather",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/great_expectations/gx_silver_weather",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "gold_clima",
                "depends_on": [
                    {
                        "task_key": "GX_silver_open_weather_map",
                    },
                    {
                        "task_key": "GX_silver_clima_tempo",
                    },
                    {
                        "task_key": "GX_silver_weather",
                    },
                    {
                        "task_key": "GX_silver_INPE",
                    },
                    {
                        "task_key": "GX_silver_weather_api",
                    },
                ],
                "run_if": "ALL_DONE",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/gold/gold",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "gold_alertas",
                "depends_on": [
                    {
                        "task_key": "gold_clima",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/gold/alerta_alagamento",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
                "notification_settings": {
                    "no_alert_for_skipped_runs": True,
                    "no_alert_for_canceled_runs": True,
                },
                "webhook_notifications": {
                    "on_success": [
                        {
                            "id": "2d1ee673-9d65-438d-a60f-17fe842a4367",
                        },
                    ],
                    "on_failure": [
                        {
                            "id": "2d1ee673-9d65-438d-a60f-17fe842a4367",
                        },
                    ],
                },
            },
            {
                "task_key": "emitir_alerta_alagamento",
                "depends_on": [
                    {
                        "task_key": "gold_alertas",
                    },
                ],
                "sql_task": {
                    "alert": {
                        "alert_id": "1f68e378-6442-4692-830f-c6d13e66c4f7",
                        "subscriptions": [
                            {
                                "user_name": "lucas.berta@cwi.com.br",
                            },
                            {
                                "user_name": "lucas.bringmann@cwi.com.br",
                            },
                            {
                                "user_name": "lucas.zorn@cwi.com.br",
                            },
                            {
                                "user_name": "evelise.dias@cwi.com.br",
                            },
                            {
                                "user_name": "gabriel.rost@cwi.com.br",
                            },
                        ],
                    },
                    "warehouse_id": "a8e3c3cbf83b7fd7",
                },
                "notification_settings": {
                    "no_alert_for_skipped_runs": True,
                    "no_alert_for_canceled_runs": True,
                },
                "webhook_notifications": {
                    "on_success": [
                        {
                            "id": "2d1ee673-9d65-438d-a60f-17fe842a4367",
                        },
                        {
                            "id": "940607a1-fb72-4128-af5b-2a1c80039afc",
                        },
                    ],
                },
            },
            {
                "task_key": "gold_clima_alagementos",
                "depends_on": [
                    {
                        "task_key": "gold_clima",
                    },
                    {
                        "task_key": "GX_silver_chuvas_criticas",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/gold/clima_alagamento",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "gold_previsao_clima",
                "depends_on": [
                    {
                        "task_key": "gold_clima",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/gold/previsao_clima",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
            {
                "task_key": "newsletter_aqualert",
                "depends_on": [
                    {
                        "task_key": "gold_previsao_clima",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lucas.berta@cwi.com.br/grupo-01/src/cwi_rocket/main_newsletter_aqualert",
                    "source": "WORKSPACE",
                },
                "existing_cluster_id": "0521-163119-ff71kxrt",
            },
        ],
        "queue": {
            "enabled": True,
        },
    }
)

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.jobs.reset(new_settings=Grupo01, job_id=746861864204385)
# or create a new job using: w.jobs.create(**Grupo01.as_shallow_dict())
