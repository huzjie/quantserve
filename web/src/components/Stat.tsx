import './Stat.css'

export default function Stat({ label, value, accent }: {
  label: string; value: string; accent?: boolean
}) {
  return (
    <div className="stat">
      <div className="stat-value" style={accent ? { color: 'var(--red)' } : undefined}>
        {value}
      </div>
      <div className="stat-label">{label}</div>
    </div>
  )
}
