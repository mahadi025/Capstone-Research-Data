import { Link } from "react-router-dom"

export default function ListData({ data }) {

    return (
        <Link to={`/capstone/${data.id}`}>
            <div className="data-list-item" >
                <p>Model Name: {data.model_name} Accuracy:({data.training_accuracy},{data.validation_accuracy},{data.testing_accuracy}) Epochs: {data.epochs} Batch Size: {data.batch_size} Learning Rate: {data.learning_rate}</p>
            </div>
        </Link>
    )
}