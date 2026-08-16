import hydra
from omegaconf.dictconfig import DictConfig


@hydra.main(config_path="config", config_name="config.yaml", version_base=None)
def main(config: DictConfig):
    print(config)


if __name__ == "__main__":
    main()
