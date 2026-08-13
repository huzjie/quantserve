import { ReactNode } from 'react'
import './Card.css'

export default function Card({ title, children, right }: {
  title: string; children: ReactNode; right?: ReactNode
}) {
  return (
    <section className="card">
      <header className="card-head">
        <h3>{title}</h3>
        {right}
      </header>
      <div className="card-body">{children}</div>
    </section>
  )
}
