import React, { useState } from 'react';
import PropTypes from 'prop-types';
import Editor from '@monaco-editor/react';


const DashMonacoEditor = (props) => {
    
    const {height, language, setProps, value,theme} = props;

    const setval = (currentval) => {
        setProps({
            value: currentval,
        });
    };

    return (
        <div>
            <Editor height={height} language={language} value={value} theme={theme} onChange={setval}/>
        </div>
    );
}

DashMonacoEditor.defaultProps = {};

DashMonacoEditor.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Height of the editor
     */
    height: PropTypes.string,

    /**
     * The language of the editor
     */
    language: PropTypes.string.isRequired,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
    /**
     * current code
     */
    value: PropTypes.string,
    /**
     * current theme "light","vs-dark"
     */
    theme: PropTypes.string.isRequired,
};

export default DashMonacoEditor;
