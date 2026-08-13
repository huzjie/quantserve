import './Tag.css'

export default function Tag({ children, color }: { children: string; color?: string }) {
  return <span className="tag" style={color ? { background: color } : undefined}>{children}</span>
}
