import React, {useState, useEffect} from 'react';
import api from './api';

const App = () => {

     const [data_resp, setdata_resp] = useState();

    const fetchRoot = async () => {
        const res = await api.get('/root');
        setdata_resp(res.data);
    }

    useEffect(() => {
        // alert("I LOVE You");
        
    }
    );
    
    return (
        <div>
            <h1>{data_resp}</h1>
        </div>
    )
}

export default App;
