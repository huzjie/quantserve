import './SearchBar.css'

export default function SearchBar({ value, onChange }: {
  value: string; onChange: (v: string) => void
}) {
  return (
    <input className="search" placeholder="搜索模型 ID / 名称 / 家族…"
      value={value} onChange={(e) => onChange(e.target.value)} />
  )
}
