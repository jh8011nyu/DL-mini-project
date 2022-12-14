def get_configs():
    train_params = {
        "device": "cuda",
        "max_epoch": 50,
        "output_dir": "output"
    }

    dataset_params = {
        "train_bs": 128,
        "test_bs": 256,
    }

    model_params = {

    }

    callback_params = {
        "patience": 5,
        "save_final_model": True,
    }

    optimizer_params = {
        "lr": 0.0001,
        "type": "AdamW",
        "kwargs": {
            "weight_decay": 5e-4,
            "amsgrad": True
        }
    }

    return train_params, dataset_params, callback_params, optimizer_params
