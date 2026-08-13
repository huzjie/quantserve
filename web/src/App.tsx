import { Routes, Route, NavLink } from 'react-router-dom'
import Models from './pages/Models'
import Quantize from './pages/Quantize'
import Cluster from './pages/Cluster'
import Cost from './pages/Cost'
import './App.css'

const nav = [
  { to: '/', label: '模型库' },
  { to: '/quantize', label: '量化规划' },
  { to: '/cluster', label: '集群规划' },
  { to: '/cost', label: '成本对比' },
]

export default function App() {
  return (
    <div className="app">
      <header className="topbar">
        <div className="brand">
          <span className="logo">QS</span>
          <span>QuantServe</span>
        </div>
        <nav>
          {nav.map((n) => (
            <NavLink key={n.to} to={n.to} end={n.to === '/'}
              className={({ isActive }) => (isActive ? 'active' : '')}>
              {n.label}
            </NavLink>
          ))}
        </nav>
      </header>
      <main className="content">
        <Routes>
          <Route path="/" element={<Models />} />
          <Route path="/quantize" element={<Quantize />} />
          <Route path="/cluster" element={<Cluster />} />
          <Route path="/cost" element={<Cost />} />
        </Routes>
      </main>
    </div>
  )
}
