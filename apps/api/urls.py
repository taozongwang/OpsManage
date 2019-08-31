from django.conf.urls import url
from api.views import (assets_api,deploy_api,db_api,
                       users_api,orders_api,cron_api,
                       celery_api,cicd_api,monitor_api,
                       nav_api,wiki_api,apscehd_api,
                       ipvs_api)
urlpatterns = [
            url(r'^assets/$', assets_api.AssetList.as_view()),   
            url(r'^assets/(?P<id>[0-9]+)/$', assets_api.asset_detail),
            url(r'^assets/info/(?P<id>[0-9]+)/$', assets_api.asset_info),     
            url(r'^assets/count/$', assets_api.asset_count),     
            url(r'^assets/tags/(?P<id>[0-9]+)/$',assets_api.assets_tags),      
            url(r'^group/$', assets_api.group_list), 
            url(r'^group/(?P<id>[0-9]+)/$',assets_api.group_detail), 
            url(r'^business/last/$', assets_api.business_list),            
            url(r'^business/env/$', assets_api.env_list), 
            url(r'^business/env/(?P<id>[0-9]+)/$',assets_api.env_detail),      
            url(r'^business/tree/$', assets_api.BUSINESS_TREE_LIST.as_view()), 
            url(r'^business/nodes/$',assets_api.NODE_LIST.as_view()), 
            url(r'^business/nodes/(?P<pk>[0-9]+)/$',assets_api.NODE_DETAIL.as_view()), 
            url(r'^business/nodes/assets/(?P<pk>[0-9]+)/$', assets_api.NODES_ASSERS_DETAIL.as_view()),                               
            url(r'^tags/$', assets_api.tags_list), 
            url(r'^tags/(?P<id>[0-9]+)/$',assets_api.tags_detail),    
            url(r'^tags/assets/(?P<id>[0-9]+)/$',assets_api.tags_assets),                   
            url(r'^user/$', users_api.user_list), 
            url(r'^user/(?P<id>[0-9]+)/$',users_api.user_detail), 
            url(r'^idc/$', assets_api.idc_list), 
            url(r'^idc/(?P<id>[0-9]+)/$',assets_api.idc_detail),    
            url(r'^idc/idle/$', assets_api.idle_list), 
            url(r'^idc/idle/(?P<id>[0-9]+)/$',assets_api.idle_detail),                      
            url(r'^zone/$', assets_api.zone_list), 
            url(r'^zone/(?P<id>[0-9]+)/$',assets_api.zone_detail),   
            url(r'^raid/$', assets_api.raid_list), 
            url(r'^raid/(?P<id>[0-9]+)/$',assets_api.raid_detail),     
            url(r'^cabinet/$', assets_api.cabinet_list), 
            url(r'^cabinet/(?P<id>[0-9]+)/$',assets_api.cabinet_detail),   
            url(r'^line/$', assets_api.line_list), 
            url(r'^line/(?P<id>[0-9]+)/$',assets_api.line_detail),                         
            url(r'^server/$', assets_api.asset_server_list), 
            url(r'^server/(?P<id>[0-9]+)/$', assets_api.asset_server_detail), 
            url(r'^net/$', assets_api.asset_net_list), 
            url(r'^net/(?P<id>[0-9]+)/$', assets_api.asset_net_detail),    
            url(r'^inventory/$', deploy_api.inventory_list),
            url(r'^inventory/(?P<id>[0-9]+)/$', deploy_api.inventory_detail),
            url(r'^inventory/groups/(?P<id>[0-9]+)/$', deploy_api.deploy_inventory_groups),
            url(r'^inventory/groups/query/(?P<id>[0-9]+)/$', deploy_api.deploy_inventory_groups_query),
            url(r'^sched/cron/$', cron_api.cron_list),
            url(r'^sched/cron/(?P<id>[0-9]+)/$', cron_api.cron_detail),
            url(r'^sched/apsched/node/$', apscehd_api.node_list),
            url(r'^sched/apsched/count/$', apscehd_api.ApschedCount.as_view()), 
            url(r'^sched/apsched/jobs/$', apscehd_api.ApschedNodeJobs.as_view()),  
            url(r'^sched/apsched/logs/$', apscehd_api.ApschedNodeJobsLogs.as_view()), 
            url(r'^v1/sched/apsched/jobs/$', apscehd_api.ApschedNodeJobsQuery.as_view()), 
            url(r'^v1/sched/apsched/logs/$', apscehd_api.ApschedNodeJobsRecord.as_view()),
            url(r'^sched/intervals/$', celery_api.celery_intervals_list),
            url(r'^sched/intervals/(?P<id>[0-9]+)/$', celery_api.celery_intervals_detail),
            url(r'^sched/crontab/$', celery_api.celery_crontab_list),
            url(r'^sched/crontab/(?P<id>[0-9]+)/$', celery_api.celery_crontab_detail),    
            url(r'^sched/celery/$', celery_api.celery_task_list),
            url(r'^sched/celery/(?P<id>[0-9]+)/$', celery_api.celery_task_detail),    
            url(r'^sched/celery/result/$', celery_api.CeleryTaskResultList.as_view()),  
            url(r'^sched/celery/result/(?P<id>[0-9]+)/$', celery_api.celery_task_result_detail),                
            url(r'^host/vars/(?P<id>[0-9]+)/$', deploy_api.deploy_host_vars),
            url(r'^db/config/$', db_api.db_list),
            url(r'^db/tree/$', db_api.db_tree),
            url(r'^db/query/$', db_api.DBUserQuery.as_view()),
            url(r'^db/config/(?P<id>[0-9]+)/$', db_api.db_detail),
            url(r'^db/status/(?P<id>[0-9]+)/$', db_api.db_status),
            url(r'^db/org/(?P<id>[0-9]+)/$', db_api.db_org),
            url(r'^orders/list/$', orders_api.OrdersPaginator.as_view()),
            url(r'^orders/(?P<id>[0-9]+)/$', orders_api.order_detail),
            url(r'^orders/count/$', orders_api.order_count),
            url(r'^orders/notice/$', orders_api.notice_config),
            url(r'^orders/notice/(?P<id>[0-9]+)/$', orders_api.notice_config_detail),
            url(r'^sql/custom/$', db_api.sql_custom_list),
            url(r'^sql/custom/(?P<id>[0-9]+)/$', db_api.sql_custom_detail), 
            url(r'^apps/list/$', cicd_api.project_list),   
            url(r'^apps/list/(?P<id>[0-9]+)/$', cicd_api.project_detail), 
            url(r'^apps/logs/$', cicd_api.AppsLogPaginator.as_view()),  
            url(r'^apps/log/(?P<id>.+)/$', cicd_api.project_log_detail), 
            url(r'^apps/logs/detail/(?P<id>.+)/$', cicd_api.AppsLogRecord.as_view()),  
            url(r'^apps/count/$', cicd_api.AppsCounts.as_view()), 
            url(r'^apps/roles/$', cicd_api.apps_roles_list),    
            url(r'^apps/roles/(?P<id>[0-9]+)/$', cicd_api.apps_roles_detail),                       
            url(r'^logs/ansible/model/$', deploy_api.DeployModelLogPaginator.as_view()),
            url(r'^logs/ansible/model/(?P<id>[0-9]+)/$', deploy_api.modelLogsdetail),
            url(r'^logs/ansible/playbook/$', deploy_api.DeployPlaybookLogPaginator.as_view()),            
            url(r'^logs/ansible/playbook/(?P<id>[0-9]+)/$', deploy_api.playbookLogsdetail),            
            url(r'^logs/sql/$', db_api.DatabaseExecuteHistroy.as_view()),    
            url(r'^monitor/assets/(?P<id>.+)/$', monitor_api.AssetsMonitor.as_view()),  
            url(r'^monitor/apps/(?P<id>.+)/$', monitor_api.AppsMonitor.as_view()), 
            url(r'^nav/type/$', nav_api.navtype_list), 
            url(r'^nav/type/(?P<id>[0-9]+)/$', nav_api.navtype_detail),     
            url(r'^nav/number/$', nav_api.navnumber_list), 
            url(r'^nav/number/(?P<id>[0-9]+)/$', nav_api.navnumber_detail),               
            url(r'^nav/third/$', nav_api.navthird_list), 
            url(r'^nav/third/(?P<id>[0-9]+)/$', nav_api.navthird_detail),     
            url(r'^nav/third/number/$', nav_api.navthird_number_list), 
            url(r'^nav/third/number/(?P<id>[0-9]+)/$', nav_api.navthird_number_detail),             
            url(r'^wiki/tag/$', wiki_api.tag_list),
            url(r'^wiki/tag/(?P<id>[0-9]+)/$', wiki_api.tag_detail),
            url(r'^wiki/category/$', wiki_api.category_list),
            url(r'^wiki/category/(?P<id>[0-9]+)/$', wiki_api.category_detail),   
            url(r'^wiki/archive/(?P<id>[0-9]+)/$', wiki_api.archive_detail),       
            url(r'^apply/ipvs/$', ipvs_api.IPVSLIST.as_view()),  
            url(r'^apply/ipvs/(?P<pk>[0-9]+)/$', ipvs_api.IPVSLIST_DETAIL.as_view()), 
            url(r'^apply/ipvs/rs/$', ipvs_api.IPVS_RS_LIST.as_view()),     
            url(r'^apply/ipvs/rs/(?P<pk>[0-9]+)/$', ipvs_api.IPVS_RS_LIST_DETAIL.as_view()),   
            url(r'^apply/ipvs/tree/$', ipvs_api.ipvs_tree),  
            url(r'^apply/ipvs/tree/business/(?P<id>[0-9]+)/$', ipvs_api.ipvs_tree_business),
            url(r'^apply/ipvs/rs/assets/$', ipvs_api.ipvs_assets),                 
            url(r'^apply/ipvs/ns/$', ipvs_api.IPVS_NS_LIST.as_view()),     
            url(r'^apply/ipvs/ns/(?P<pk>[0-9]+)/$', ipvs_api.IPVS_NS_LIST_DETAIL.as_view()),                                                                 
    ]    