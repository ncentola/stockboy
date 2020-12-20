import React from 'react';
import './Switch.css';

const Switch = ({ isOn, handleToggle, onColor, onClick }) => {
  return (
    <>
      <input
        checked={isOn}
        onChange={handleToggle}
        onClick={onClick}
        className="react-switch-checkbox"
        id={"switch-new"}
        type="checkbox"
      />
      <label
        style={{ background: isOn && onColor }}
        className="react-switch-label"
        htmlFor={"switch-new"}
      >
        <span className="react-switch-button" />
      </label>
    </>
  );
};

export default Switch;
