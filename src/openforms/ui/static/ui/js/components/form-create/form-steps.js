import React from "react";
import {post} from "./api";
import {Form as FormioForm} from "react-formio";

// Just need form definition
// or
// TODO Create new Form definition


const CreateStepForm = ({configuration}) => {
    return (
        <div>
            <h2>Step</h2>
            <FormioForm form={configuration}/>
        </div>
    );
};

export default CreateStepForm;