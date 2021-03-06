BEGIN;
ALTER TABLE auth_group ENGINE=InnoDB;
ALTER TABLE auth_group_permissions ENGINE=InnoDB;
ALTER TABLE auth_message ENGINE=InnoDB;
ALTER TABLE auth_permission ENGINE=InnoDB;
ALTER TABLE auth_user ENGINE=InnoDB;
ALTER TABLE auth_user_groups ENGINE=InnoDB;
ALTER TABLE auth_user_user_permissions ENGINE=InnoDB;

-- Comment the next six tables for the original version.
ALTER TABLE authtoken_token ENGINE=InnoDB;
ALTER TABLE dcolumns_collectionbase ENGINE=InnoDB;
ALTER TABLE dcolumns_columncollection ENGINE=InnoDB;
ALTER TABLE dcolumns_columncollection_dynamic_column ENGINE=InnoDB;
ALTER TABLE dcolumns_dynamiccolumn ENGINE=InnoDB;
ALTER TABLE dcolumns_keyvalue ENGINE=InnoDB;

ALTER TABLE django_admin_log ENGINE=InnoDB;
ALTER TABLE django_content_type ENGINE=InnoDB;
ALTER TABLE django_migrations ENGINE=InnoDB;
ALTER TABLE django_session ENGINE=InnoDB;
ALTER TABLE django_site ENGINE=InnoDB;

-- Comment the next two tables for the original version.
ALTER TABLE guardian_groupobjectpermission ENGINE=InnoDB;
ALTER TABLE guardian_userobjectpermission ENGINE=InnoDB;

ALTER TABLE items_category ENGINE=InnoDB;
ALTER TABLE items_cost ENGINE=InnoDB;
ALTER TABLE items_currency ENGINE=InnoDB;
ALTER TABLE items_distributor ENGINE=InnoDB;
ALTER TABLE items_item ENGINE=InnoDB;
ALTER TABLE items_item_categories ENGINE=InnoDB;
ALTER TABLE items_item_location_code ENGINE=InnoDB;
ALTER TABLE items_manufacturer ENGINE=InnoDB;
ALTER TABLE items_specification ENGINE=InnoDB;
ALTER TABLE maintenance_locationcodecategory ENGINE=InnoDB;
ALTER TABLE maintenance_locationcodedefault ENGINE=InnoDB;

-- Comment the next three tables for the original version.
ALTER TABLE projects_project ENGINE=InnoDB;
ALTER TABLE projects_project_managers ENGINE=InnoDB;
ALTER TABLE projects_project_members ENGINE=InnoDB;
ALTER TABLE regions_country ENGINE=InnoDB;
ALTER TABLE regions_region ENGINE=InnoDB;

-- Comment the next two tables for the original version.
ALTER TABLE user_profiles_userprofile ENGINE=InnoDB;
ALTER TABLE user_profiles_userprofile_projects ENGINE=InnoDB;
COMMIT;
