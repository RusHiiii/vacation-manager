{ pkgs, config, ... }:

let
  db_user = "vacation_manager";
  db_name = "vacation_manager";
  db_pass = "pass";
in
{
  languages = {
    javascript = {
      enable = true;
      package = pkgs.nodejs_20;
    };
    python = {
      enable = true;
      version = "3.11";
      poetry = {
        enable = true;
        install = {
          enable = true;
          installRootPackage = false;
          onlyInstallRootPackage = false;
          compile = false;
          quiet = false;
          groups = [ ];
          ignoredGroups = [ ];
          onlyGroups = [ ];
          extras = [ ];
          allExtras = false;
          verbosity = "no";
        };
        activate.enable = true;
        package = pkgs.poetry;
      };
    };
  };

  services = {
    postgres = {
      enable = true;
      package = pkgs.postgresql_15;
      listen_addresses = "127.0.0.1";
      initialScript = "CREATE ROLE ${db_user} WITH LOGIN SUPERUSER PASSWORD '${db_pass}';";
      initialDatabases = [{ name = db_name; }];
    };
  };

  env = {
    DJANGO_DEBUG = "true";
    STATIC_ROOT = "${config.devenv.state}/static";
    DATABASE_USERNAME = "${db_user}";
    DATABASE_PASSWORD = "${db_pass}";
    DATABASE_HOST = "127.0.0.1";
    DATABASE_PORT = "5432";
  };

  processes.runserver = {
    exec = "python vacation_manager/manage.py runserver";
    process-compose.depends_on.postgres.condition = "process_healthy";
  };

  processes.tailwind = {
    exec = "python vacation_manager/manage.py tailwind start";
    process-compose.depends_on.postgres.condition = "process_healthy";
    };
}
