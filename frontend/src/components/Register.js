import React, { useState } from 'react';
import axios from 'axios';

const CreateClientForm = () => {
  const [schemaName, setSchemaName] = useState('');
  const [clientName, setClientName] = useState('');
  const [paidUntil, setPaidUntil] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Create the client object
      const clientData = {
        schema_name: schemaName,
        name: clientName,
        paid_until: paidUntil,
        on_trial: false,
      };

      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios.defaults.xsrfCookieName = "csrftoken";
      axios.defaults.withCredentials = true;

      // Send the request to create the client
      const response = await axios.post('accounts/api/tenants/', clientData);

      // Handle the response as needed
      console.log(response.data);

      // Reset the form
      setSchemaName('');
      setClientName('');
      setPaidUntil('');
    } catch (error) {
      // Handle any errors
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Schema Name:
        <input type="text" value={schemaName} onChange={(e) => setSchemaName(e.target.value)} />
      </label>
      <label>
        Client Name:
        <input type="text" value={clientName} onChange={(e) => setClientName(e.target.value)} />
      </label>
      <label>
        Paid Until:
        <input type="date" value={paidUntil} onChange={(e) => setPaidUntil(e.target.value)} />
      </label>
      <button type="submit">Create Client</button>
    </form>
  );
};

export default CreateClientForm;
