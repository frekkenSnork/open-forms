import React, {useState, useEffect, Fragment} from "react";
import PropTypes from 'prop-types';
import useAsync from 'react-use/esm/useAsync';
import {get, post, put, destroy} from './api';
import DeleteFormStepModal from './delete-form-step-modal';


const EditForm = ({formUUID}) => {

    const [stepForms, setStepForms] = useState([]);
    const [stepFormValues, setStepFormValues] = useState({});
    const [formStepsToDelete, setFormStepsToDelete] = useState([]);
    const [formStepsToUpdate, setFormStepsToUpdate] = useState([]);
    const [isDeleteFormStepModalOpen, setIsDeleteFormStepModalOpen] = useState(false);
    const [deleteFormStepUuid, setDeleteFormStepUuid] = useState(null);
    const [deleteFormStepNumber, setDeleteFormStepNumber] = useState(null);

    const handleDeleteFormStepModalClose = () => setIsDeleteFormStepModalOpen(false);

    const {loading: formLoading, value: formValue, error: formError} = useAsync(
        async () => await get(`/api/v1/forms/${formUUID}`)
    );

    const {loading: formDefinitionLoading, value: formDefinitionValues, error: formDefinitionError} = useAsync(
        async () => await get('/api/v1/form-definitions')
    );

    const {loading: formStepsLoading, value: formStepsValues, error: formStepsError} = useAsync(
        async () => await get(`/api/v1/forms/${formUUID}/steps`)
    );

    useEffect(() => {
        if (formStepsValues) {
            const initialStepFormsValues = [];

            formStepsValues.forEach((formStepsValue, index) => {
                initialStepFormsValues.push(
                    <Fragment key={index}>
                        <td>
                            <select name="formDefinitions"
                                    defaultValue={formStepsValue.formDefinition}
                                    onChange={event => {
                                        setFormStepsToUpdate(previousState => {
                                            previousState[formStepsValue.uuid] = event.target.value;
                                            return previousState;
                                        });
                                    }}>
                                {formDefinitionValues.results.map(definition => {
                                    return <option key={definition.slug} value={definition.url}>{definition.name}</option>
                                })}
                            </select>
                            <a
                                className="related-widget-wrapper-link delete-related"
                                style={{opacity: 0.8}}
                                onClick={_ => {
                                    setDeleteFormStepUuid(formStepsValue.uuid);
                                    setIsDeleteFormStepModalOpen(true);
                                    // setStepFormValues(previousState => {
                                    //     delete previousState[index + 1];
                                    //     return previousState;
                                    // });
                                    // setFormStepsToUpdate(previousState => {
                                    //     delete previousState[formStepsValue.uuid];
                                    //     return previousState;
                                    // });
                                    // setStepForms(previousState => previousState.filter(element => element.key !== index.toString()));
                                    // setFormStepsToDelete([...formStepsToDelete, formStepsValue.uuid]);
                            }}>
                                <img src="/static/admin/img/icon-deletelink.svg" alt="Verwijderen"/>
                            </a>
                        </td>
                    </Fragment>
                )
            });

            setStepForms(initialStepFormsValues);
        }
    }, [formStepsValues]);

    const getNewStep = () => {
        return (
            <Fragment key={stepForms.length}>
                <td>
                    <select name="formDefinitions" onChange={event => {
                        setStepFormValues(previousState => {
                            previousState[stepForms.length+1] = event.target.value;
                            return previousState;
                        });
                    }}>
                        <option key='---' value='---'>---</option>
                        {formDefinitionValues.results.map(definition => {
                            return <option key={definition.slug} value={definition.url}>{definition.name}</option>
                        })}
                    </select>
                    <a
                        className="related-widget-wrapper-link delete-related"
                        style={{opacity: 0.8}}
                        onClick={_ => {
                            // TODO Use delete-form-step-modal here
                            setStepFormValues(previousState => {
                                delete previousState[stepForms.length + 1];
                                return previousState;
                        });
                        setStepForms(previousState => previousState.filter(element => element.key !== stepForms.length.toString()));
                    }}>
                        <img src="/static/admin/img/icon-deletelink.svg" alt="Verwijderen"/>
                    </a>
                </td>
            </Fragment>
        )
    };

    return (
        <div className="card">
            <header className="card__header">
                {formValue &&
                    <h1 className="title">Edit Form: {formValue.name}</h1>
                }
            </header>
            <div>
                <div className="inline-group tabular inline-related">
                    <fieldset className="module">
                        <h2>Form Steps</h2>
                        <table>
                            <thead>
                                <tr>
                                    <th>Order</th>
                                    <th>Form Definition</th>
                                </tr>
                            </thead>
                            <tbody>
                                {stepForms.map((stepForm, index) => {
                                    return (
                                        <tr key={index}>
                                            <td>{index}</td>
                                            {stepForm}
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                    </fieldset>
                    <div className="submit-row">
                        <button
                            style={{float: 'right', marginLeft: 8}}
                            className="button"
                            onClick={_ => {
                                setStepForms([...stepForms, getNewStep()]);
                            }}
                        >
                            Add Step
                        </button>
                        <button
                            style={{float: 'right', marginLeft: 8}}
                            className="button"
                            onClick={_ => {
                                for (const [stepUUID, formDefinition] of Object.entries(formStepsToUpdate)) {
                                    const data = {
                                        "formDefinition": formDefinition
                                    };
                                    put(`/api/v1/forms/${formUUID}/steps/${stepUUID}`, data).then(e => {
                                        console.log(e);
                                    });
                                }

                                for (const [key, formDefinition] of Object.entries(stepFormValues)) {
                                    const data = {
                                        "formDefinition": formDefinition
                                    };
                                    post(`/api/v1/forms/${formUUID}/steps`, data).then(e => {
                                        console.log(e);
                                    });
                                }
                            }}
                        >
                            Submit
                        </button>
                    </div>
                </div>
            </div>
            <DeleteFormStepModal
                formUUID={formUUID}
                formStepUUID={deleteFormStepUuid}
                isOpen={isDeleteFormStepModalOpen}
                handleCloseFunction={handleDeleteFormStepModalClose}
            />
        </div>
    );
};

EditForm.propTypes = {
    formUUID: PropTypes.string.isRequired,
};

export default EditForm;
