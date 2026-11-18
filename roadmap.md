


django-learning/
│
├── 00_setup_environment/
│   ├── python_venv.md
│   ├── django_installation.md
│   ├── django_version.md
│   ├── requirements.txt
│   ├── project_setup.md
│   └── gitignore.md
│
├── 01_django_basics/
│   ├── django_intro.md
│   ├── project_vs_app.md
│   ├── django_structure.md
│   ├── manage_py.md
│   ├── settings_py.md
│   ├── apps_py.md
│   ├── migrations_folder.md
│   ├── request_response.md
│   ├── development_server.md
│   └── first_django_project/
│
├── 02_urls_and_views/
│   ├── urls_basics.py
│   ├── path.py
│   ├── url_parameters.py
│   ├── dynamic_urls.py
│   ├── named_urls.py
│   ├── include_urls.py
│   ├── httpresponse.py
│   ├── function_based_views.py
│   ├── request_object.py
│   ├── redirect.py
│   └── exercises/
│
├── 03_templates/
│   ├── template_basics.md
│   ├── render_template.py
│   ├── template_variables.md
│   ├── template_if.py
│   ├── template_for.py
│   ├── template_filters.md
│   ├── template_tags.md
│   ├── template_comments.md
│   ├── template_inheritance.md
│   ├── base_template.md
│   ├── extends_block.md
│   ├── include_template.md
│   └── exercises/
│
├── 04_static_files/
│   ├── static_intro.md
│   ├── css.md
│   ├── javascript.md
│   ├── images.md
│   ├── static_url.md
│   ├── staticfiles_dirs.md
│   ├── load_static.md
│   └── exercises/
│
├── 05_models/
│   ├── model_basics.py
│   ├── model_structure.md
│   ├── charfield.py
│   ├── integerfield.py
│   ├── booleanfield.py
│   ├── textfield.py
│   ├── datefield.py
│   ├── datetimefield.py
│   ├── decimalfield.py
│   ├── primary_keys.md
│   ├── default_values.md
│   ├── null_vs_blank.md
│   ├── unique.md
│   ├── choices.md
│   ├── model_str_method.py
│   └── exercises/
│
├── 06_migrations/
│   ├── migration_intro.md
│   ├── makemigrations.md
│   ├── migrate.md
│   ├── migration_files.md
│   ├── changing_models.md
│   ├── adding_fields.md
│   ├── removing_fields.md
│   ├── migration_dependencies.md
│   └── exercises/
│
├── 07_django_orm_basics/
│   ├── orm_intro.md
│   ├── objects_manager.md
│   ├── create.py
│   ├── save.py
│   ├── all.py
│   ├── get.py
│   ├── filter.py
│   ├── exclude.py
│   ├── update.py
│   ├── delete.py
│   ├── first_last.py
│   ├── exists.py
│   ├── count.py
│   ├── order_by.py
│   ├── values.py
│   ├── values_list.py
│   ├── get_or_create.py
│   └── exercises/
│
├── 08_orm_lookups/
│   ├── exact.py
│   ├── iexact.py
│   ├── contains.py
│   ├── icontains.py
│   ├── startswith.py
│   ├── endswith.py
│   ├── gt_gte.py
│   ├── lt_lte.py
│   ├── in_lookup.py
│   ├── range.py
│   ├── isnull.py
│   ├── date_lookups.py
│   └── exercises/
│
├── 09_orm_advanced/
│   ├── q_objects.py
│   ├── f_expressions.py
│   ├── conditional_queries.py
│   ├── aggregation.md
│   ├── count_sum_avg.py
│   ├── min_max.py
│   ├── aggregate.py
│   ├── annotate.py
│   ├── distinct.py
│   ├── queryset_slicing.py
│   ├── lazy_querysets.md
│   ├── raw_sql.md
│   └── exercises/
│
├── 10_relationships/
│   ├── relationships_intro.md
│   ├── foreignkey.py
│   ├── on_delete.md
│   ├── one_to_one.py
│   ├── many_to_many.py
│   ├── forward_relationships.py
│   ├── reverse_relationships.py
│   ├── related_objects.py
│   ├── relationship_queries.py
│   ├── select_related.py
│   ├── prefetch_related.py
│   └── exercises/
│
├── 11_forms/
│   ├── html_forms.md
│   ├── get_vs_post.md
│   ├── request_get.py
│   ├── request_post.py
│   ├── django_form.py
│   ├── form_fields.py
│   ├── form_validation.py
│   ├── custom_validation.py
│   ├── form_errors.md
│   ├── modelform.py
│   ├── csrf.md
│   └── exercises/
│
├── 12_crud/
│   ├── create.md
│   ├── read.md
│   ├── update.md
│   ├── delete.md
│   ├── detail_page.md
│   ├── redirect.md
│   ├── confirmation_page.md
│   └── student_management_project/
│
├── 13_url_routing_advanced/
│   ├── path_converters.md
│   ├── int_converter.md
│   ├── slug_converter.md
│   ├── uuid_converter.md
│   ├── reverse.md
│   ├── reverse_in_templates.md
│   ├── url_tag.md
│   └── namespaces.md
│
├── 14_authentication/
│   ├── user_model.md
│   ├── create_user.py
│   ├── superuser.md
│   ├── login.py
│   ├── logout.py
│   ├── authentication_forms.md
│   ├── request_user.md
│   ├── login_required.md
│   ├── sessions.md
│   ├── password_hashing.md
│   ├── registration.md
│   ├── password_change.md
│   ├── password_reset.md
│   ├── permissions.md
│   ├── groups.md
│   └── exercises/
│
├── 15_django_admin/
│   ├── admin_intro.md
│   ├── register_model.py
│   ├── list_display.py
│   ├── list_filter.py
│   ├── search_fields.py
│   ├── ordering.py
│   ├── readonly_fields.py
│   ├── fieldsets.md
│   └── exercises/
│
├── 16_messages_sessions_cookies/
│   ├── messages.md
│   ├── success_message.py
│   ├── error_message.py
│   ├── warning_message.py
│   ├── sessions.md
│   ├── session_data.py
│   ├── cookies.md
│   └── exercises/
│
├── 17_class_based_views/
│   ├── cbv_intro.md
│   ├── templateview.py
│   ├── listview.py
│   ├── detailview.py
│   ├── createview.py
│   ├── updateview.py
│   ├── deleteview.py
│   ├── mixins.md
│   └── exercises/
│
├── 18_files_and_media/
│   ├── file_upload.md
│   ├── image_upload.md
│   ├── filefield.py
│   ├── imagefield.py
│   ├── media_root.md
│   ├── media_url.md
│   ├── upload_forms.py
│   └── exercises/
│
├── 19_postgresql/
│   ├── postgresql_setup.md
│   ├── django_postgresql.md
│   ├── database_settings.md
│   ├── postgres_migrations.md
│   ├── django_orm_vs_sql.md
│   ├── transactions.md
│   ├── constraints.md
│   └── exercises/
│
├── 20_testing/
│   ├── testing_intro.md
│   ├── django_testcase.py
│   ├── model_tests.py
│   ├── view_tests.py
│   ├── url_tests.py
│   ├── form_tests.py
│   ├── authentication_tests.py
│   ├── test_client.py
│   ├── pytest_intro.md
│   ├── pytest_django.md
│   └── testing_project/
│
├── 21_security/
│   ├── security_intro.md
│   ├── csrf.md
│   ├── xss.md
│   ├── sql_injection.md
│   ├── clickjacking.md
│   ├── password_security.md
│   ├── secret_key.md
│   ├── debug_mode.md
│   ├── allowed_hosts.md
│   ├── environment_variables.md
│   └── security_checklist.md
│
├── 22_middleware/
│   ├── middleware_intro.md
│   ├── built_in_middleware.md
│   ├── request_middleware.py
│   ├── response_middleware.py
│   ├── custom_middleware.py
│   └── exercises/
│
├── 23_signals/
│   ├── signals_intro.md
│   ├── pre_save.py
│   ├── post_save.py
│   ├── pre_delete.py
│   ├── post_delete.py
│   ├── signal_registration.md
│   └── exercises/
│
├── 24_advanced_django/
│   ├── custom_managers.md
│   ├── custom_querysets.md
│   ├── model_methods.md
│   ├── model_meta.md
│   ├── database_indexes.md
│   ├── database_constraints.md
│   ├── transactions.md
│   ├── atomic.md
│   ├── pagination.md
│   ├── caching.md
│   ├── logging.md
│   ├── custom_management_commands.md
│   └── advanced_project/
│
├── 25_django_rest_framework/
│   ├── rest_api_intro.md
│   ├── http_methods.md
│   ├── http_status_codes.md
│   ├── serializers.py
│   ├── serializer_validation.py
│   ├── modelserializer.py
│   ├── apiview.py
│   ├── generic_views.py
│   ├── viewsets.py
│   ├── routers.py
│   ├── api_crud.md
│   ├── authentication.md
│   ├── permissions.md
│   ├── pagination.md
│   ├── filtering.md
│   ├── searching.md
│   ├── api_errors.md
│   ├── jwt.md
│   └── drf_project/
│
├── 26_api_testing/
│   ├── postman_basics.md
│   ├── api_requests.md
│   ├── drf_testing.md
│   ├── authenticated_api_tests.py
│   └── api_test_project/
│
├── 27_performance/
│   ├── query_optimization.md
│   ├── n_plus_one.md
│   ├── select_related.md
│   ├── prefetch_related.md
│   ├── database_indexes.md
│   ├── pagination.md
│   ├── caching.md
│   ├── django_debug_toolbar.md
│   └── exercises/
│
├── 28_deployment/
│   ├── production_settings.md
│   ├── environment_variables.md
│   ├── requirements.txt
│   ├── gunicorn.md
│   ├── nginx_basics.md
│   ├── static_files.md
│   ├── media_files.md
│   ├── postgres_production.md
│   ├── logging.md
│   └── deployment_checklist.md
│
├── 29_docker/
│   ├── docker_intro.md
│   ├── dockerfile.md
│   ├── docker_images.md
│   ├── docker_containers.md
│   ├── ports.md
│   ├── volumes.md
│   ├── environment_variables.md
│   ├── docker_compose.md
│   ├── django_docker.md
│   ├── django_postgres_docker.md
│   └── docker_project/
│
├── 30_git_ci_cd/
│   ├── django_git.md
│   ├── gitignore.md
│   ├── environment_files.md
│   ├── github_actions.md
│   ├── run_tests_in_ci.md
│   ├── pull_request_checks.md
│   └── ci_project/
│
├── 31_ai_backend/
│   ├── django_ai_intro.md
│   ├── llm_api_intro.md
│   ├── llm_api_integration.py
│   ├── ai_api_endpoint.py
│   ├── prompt_handling.md
│   ├── streaming_responses.md
│   ├── embeddings_intro.md
│   ├── vector_database_intro.md
│   ├── rag_intro.md
│   ├── django_rag_api.md
│   ├── background_ai_tasks.md
│   └── ai_backend_project/
│
├── 32_projects/
│   ├── 01_student_management/
│   ├── 02_blog/
│   ├── 03_authentication_app/
│   ├── 04_inventory_api/
│   ├── 05_task_management_api/
│   ├── 06_ecommerce_backend/
│   └── 07_ai_rag_backend/
│
└── README.md










