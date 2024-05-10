from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('carrier_advice', views.carrier_advice, name='carrier_advice'),
    path('employee_signup', views.employee_signup, name='employee_signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('employee_dashboard', views.employee_dashboard, name='employee_dashboard'),
    path('employee_process_job_application', views.employee_process_job_application, name='employee_process_job_application'),
    path('employee_process_job_application_external', views.employee_process_job_application_external, name='employee_process_job_application_external'),
    path('employee_single_offer', views.employee_single_offer, name='employee_single_offer'),
    path('employee_single_offer_offline', views.employee_single_offer_offline, name='employee_single_offer_offline'),
    path('employee_application_info', views.employee_application_info, name='employee_application_info'),
    path('employee_offers', views.employee_offers, name='employee_offers'),
    path('employee_offers_offline', views.employee_offers_offline, name='employee_offers_offline'),
    path('employee_all_offers', views.employee_all_offers, name='employee_all_offers'),
    path('employee_filter_offers', views.employee_filter_offers, name='employee_filter_offers'),
    path('employee_filter_offers_offline', views.employee_filter_offers_offline, name='employee_filter_offers_offline'),
    path('employee_single_notification', views.employee_single_notification, name='employee_single_notification'),
    path('employee_notifications', views.employee_notifications, name='employee_notifications'),
    path('employee_view_all_notifications', views.employee_view_all_notifications, name='employee_view_all_notifications'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('employee_profile', views.employee_profile, name='employee_profile'),
    path('employee_chat', views.employee_chat, name='employee_chat'),
    path('employee_chat_clear', views.employee_chat_clear, name='employee_chat_clear'),
    path('employee_chat_delete', views.employee_chat_delete, name='employee_chat_delete'),
    path('employee_chat_warn', views.employee_chat_warn, name='employee_chat_warn'),
    path('employee_private_chat', views.employee_private_chat, name='employee_private_chat'),
    path('reloadprivatechat', views.reloadprivatechat, name='reloadprivatechat'),
    path('reloadprivatechat_two', views.reloadprivatechat_two, name='reloadprivatechat_two'),
    path('send_message', views.send_message, name='send_message'),
    path('employer_chat', views.employer_chat, name='employer_chat'),
    path('employer_private_chat', views.employer_private_chat, name='employer_private_chat'),
    path('employer_reloadprivatechat', views.employer_reloadprivatechat, name='employer_reloadprivatechat'),
    path('employer_send_message', views.employer_send_message, name='employer_send_message'),
    path('get_profile', views.get_profile, name='get_profile'),
    path('employer_signup', views.employer_signup, name='employer_signup'),
    path('employer_dashboard', views.employer_dashboard, name='employer_dashboard'),
    path('employer_jobs', views.employer_jobs, name='employer_jobs'),
    path('employer_single_job', views.employer_single_job, name='employer_single_job'),
    path('employer_single_job_applicant', views.employer_single_job_applicant, name='employer_single_job_applicant'),
    path('employer_delete_job/<str:id_value>/', views.employer_delete_job, name='employer_delete_job'),
    path('employer_create_job', views.employer_create_job, name='employer_create_job'),
    path('create_roles', views.create_roles, name='create_roles'),
    path('create_categories', views.create_categories, name='create_categories'),
    path('create_requirement', views.create_requirement, name='create_requirement'),
    path('employer_profile', views.employer_profile, name='employer_profile'),
    path('reject_job_application', views.reject_job_application, name='reject_job_application'),
    path('accept_job_application', views.accept_job_application, name='accept_job_application'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('employer_edit_profile', views.employer_edit_profile, name='employer_edit_profile'),
    path('edit_bio', views.editbio, name='edit_bio'),
    path('employer_edit_bio', views.employer_editbio, name='employer_edit_bio'),
    path('create_skill', views.addskill, name='create_skill'),
    path('create_education', views.addeducation, name='create_education'),
    path('create_experience', views.addexperience, name='create_experience'),
    path('deleteEducation/<str:value_id>/', views.deleteeducation, name='deleteEducation'),
    path('deleteExperience/<str:value_id>/', views.deleteexperience, name='deleteExperience'),
    path('deleteSkill/<str:value_id>/', views.deleteskill, name='deleteSkill'),
    path('upload_resume', views.upload_cv, name='upload_resume'),
    path('upload_profile_pic', views.upload_profile_picture, name='upload_profile_pic'),
    path('viewprofile/<str:user_id>/', views.viewprofile, name='viewprofile'),
    path('jobview/<str:job_id>/', views.jobview, name='jobview'),
    path('unsubscribe/<str:unique_id>/', views.jobview, name='jobview'),
    path('cover_letter_viewer/<str:application_id>/', views.cover_letter_viewer, name='cover_letter_viewer'),
    path('job_board', views.job_board, name='job_board'),
    path('job_board_all', views.job_board_all, name='job_board_all'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('login_authenticate', views.login_authenticate, name='login_authenticate'),
    path('logout', views.logout, name='logout'),
    path('sitemap', views.sitemap, name='sitemap'),
]

# path('properties/<str:text>/',views.viewProperty,name='viewProperty'),
