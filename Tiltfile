load("ext://helm_remote", "helm_remote")
load("ext://restart_process", "docker_build_with_restart")
load("ext://secret", "secret_from_dict")
load("ext://configmap", "configmap_from_dict")

helm_remote("postgresql",
            repo_name="bitnami",
            repo_url="https://charts.bitnami.com/bitnami",
            set=["postgresqlPassword=password", "postgresqlDatabase=mev_inspect"],
)

k8s_yaml(configmap_from_dict("mev-inspect-rpc", inputs = {
    "url" : os.environ["RPC_URL"],
}))

k8s_yaml(secret_from_dict("mev-inspect-db-credentials", inputs = {
    "username" : "postgres",
    "password": "password",
    "host": "postgresql",
}))

# if using https://github.com/taarushv/trace-db
# k8s_yaml(secret_from_dict("trace-db-credentials", inputs = {
#     "username" : "username",
#     "password": "password",
#     "host": "trace-db-postgresql",
# }))

docker_build_with_restart("mev-inspect-py", ".",
    entrypoint="/app/entrypoint.sh",
    live_update=[
        sync(".", "/app"),
        run("cd /app && poetry install",
            trigger="./pyproject.toml"),
    ],
)
k8s_yaml(helm('./k8s/mev-inspect', name='mev-inspect'))
k8s_resource(workload="mev-inspect", resource_deps=["postgresql-postgresql"])

local_resource(
    'pg-port-forward',
    serve_cmd='kubectl port-forward --namespace default svc/postgresql 5432:5432',
    resource_deps=["postgresql-postgresql"]
)
