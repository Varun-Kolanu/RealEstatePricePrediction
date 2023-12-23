import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {

  const backend_url = import.meta.env.VITE_BACKEND_URL

  const [sqft, setSqft] = useState("")
  const [bath, setBath] = useState("")
  const [bhk, setBhk] = useState("")
  const [location, setLocation] = useState("")
  const [locations, setLocations] = useState([])
  const [price, setPrice] = useState("")

  const handleSubmit = (e) => {
    e.preventDefault()
    if(Number(sqft) <= 0) return toast.error('Sqft must be positive')
    if(Number(bath) < 0) return toast.error('No. of Bathrooms must be positive')
    if(Number(bhk) < 0) return toast.error('No. of BHK must be positive')

    axios.post(`${backend_url}/get_predicted_price`, {
      sqft: Number(sqft),
      bath: Number(bath),
      bhk: Number(bhk),
      location
    }).then(res => {
      setPrice(res.data.price)
    })
    .catch(err => {
      toast.error(err.response.data.error)
    })
  }

  useEffect(() => {
    axios.get(`${backend_url}/get_locations`).then(res => {
      setLocations(res.data.sort())
      setLocation(res.data.sort()[0])
    }).catch(console.error)
  }, [])

  return (
    <>
      <ToastContainer position="top-center"/>
      <form style={{ display: 'flex', flexDirection: 'column', gap: '20px' }} onSubmit={handleSubmit}>
        <input type="number" placeholder='Total Sqft' value={sqft} onChange={e => setSqft(e.target.value)} required/>
        <input type="number" placeholder='Bathrooms' value={bath} onChange={e => setBath(e.target.value)} required/>
        <input type="number" placeholder='BHK' value={bhk} onChange={e => setBhk(e.target.value)} required/>
        <select value={location} onChange={e => setLocation(e.target.value)}>
          {
            locations &&
            locations.map(loc => (
              <option key={loc} value={loc}> {loc} </option>
            ))
          }
        </select>
        <button type="submit"> Predict Price</button>
      </form>
      {
        price &&
        <div style={{marginTop: '20px'}}>
          <span style={{marginRight: '5px'}}>Predicted Price: </span>
          <button> {price} Lakh</button>
        </div>
      }
    </>
  )
}

export default App
