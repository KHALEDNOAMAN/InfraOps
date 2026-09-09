import React from 'react';

export default function Licenses() {
  const licenses = [
    { name: 'VMware vSphere', type: 'Perpetual', used: 45, total: 50, expiry: '2027-01-01' },
    { name: 'Windows Server', type: 'Core', used: 128, total: 128, expiry: '2026-12-31' },
    { name: 'Red Hat Enterprise', type: 'Subscription', used: 10, total: 50, expiry: '2026-06-15' },
  ];

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Software Licenses</h1>
        <button className="bg-cyan-600 hover:bg-cyan-700 px-4 py-2 rounded-lg font-medium">Add License</button>
      </div>

      <div className="bg-gray-900 rounded-xl border border-gray-800 overflow-hidden">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="bg-gray-800/50 text-gray-400 text-sm border-b border-gray-800">
              <th className="p-4 font-medium">Software</th>
              <th className="p-4 font-medium">Type</th>
              <th className="p-4 font-medium">Usage</th>
              <th className="p-4 font-medium">Compliance</th>
              <th className="p-4 font-medium">Expiry Date</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-800">
            {licenses.map(lic => {
              const percent = (lic.used / lic.total) * 100;
              const color = percent >= 100 ? 'bg-red-500' : percent >= 80 ? 'bg-yellow-500' : 'bg-green-500';
              return (
                <tr key={lic.name} className="hover:bg-gray-800/30">
                  <td className="p-4 font-medium">{lic.name}</td>
                  <td className="p-4 text-gray-400">{lic.type}</td>
                  <td className="p-4">{lic.used} / {lic.total}</td>
                  <td className="p-4 w-48">
                    <div className="w-full bg-gray-800 rounded-full h-2">
                      <div className={`h-full rounded-full ${color}`} style={{width: `${percent}%`}}></div>
                    </div>
                  </td>
                  <td className="p-4 text-gray-400">{lic.expiry}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
