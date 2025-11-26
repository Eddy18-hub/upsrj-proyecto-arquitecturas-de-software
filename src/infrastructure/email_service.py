
from flask_mail import Message
from flask import current_app, url_for

class EmailService:
    def send_approval_email(self, recipient_email: str, file_id: str, filename: str):
        try:
            # Genera el enlace: http://localhost:8080/approve/ID...
            approval_link = url_for('approve_file', file_id=file_id, _external=True)
            
            html_body = f"""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <style>
                    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; }}
                    .container {{ max-width: 600px; margin: 0 auto; background: #f8fafc; padding: 0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }}
                    .header {{ background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%); color: white; padding: 30px 20px; text-align: center; }}
                    .header h1 {{ margin: 0; font-size: 24px; font-weight: 700; }}
                    .content {{ padding: 30px 20px; }}
                    .message-box {{ background: #dbeafe; border-left: 4px solid #3b82f6; padding: 15px; border-radius: 6px; margin: 20px 0; }}
                    .file-info {{ background: #f1f5f9; padding: 15px; border-radius: 6px; margin: 20px 0; border: 1px solid #e2e8f0; }}
                    .file-info p {{ margin: 8px 0; font-size: 14px; }}
                    .file-name {{ font-weight: 600; color: #3b82f6; font-size: 16px; }}
                    .cta-button {{ display: inline-block; background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; padding: 14px 32px; text-decoration: none; border-radius: 6px; font-weight: bold; margin: 20px 0; text-align: center; }}
                    .cta-button:hover {{ opacity: 0.9; }}
                    .footer {{ background: #1e293b; color: #cbd5e1; text-align: center; padding: 20px; font-size: 12px; }}
                    .warning {{ color: #dc2626; font-weight: 600; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>🔐 Solicitud de Firma Digital</h1>
                    </div>
                    <div class="content">
                        <p>Estimado usuario,</p>
                        
                        <div class="message-box">
                            <p><strong>Se requiere su aprobación</strong> para firmar el siguiente archivo en el entorno de <strong>Producción</strong>.</p>
                        </div>
                        
                        <div class="file-info">
                            <p><strong>📄 Detalles del archivo:</strong></p>
                            <p class="file-name">{filename}</p>
                            <p><strong>ID:</strong> {file_id}</p>
                            <p><strong>Estado:</strong> <span style="color: #f59e0b; font-weight: bold;">Pendiente de Aprobación</span></p>
                        </div>
                        
                        <p><strong>¿Qué hacer?</strong></p>
                        <p>Para <strong>aprobar y firmar</strong> este archivo digitalmente, haga clic en el botón a continuación:</p>
                        
                        <center>
                            <a href="{approval_link}" class="cta-button">✓ APROBAR Y FIRMAR</a>
                        </center>
                        
                        <p style="margin-top: 25px; padding-top: 20px; border-top: 1px solid #e2e8f0; color: #64748b; font-size: 14px;">
                            <span class="warning">⚠️ Importante:</span> Si usted no solicitó esta aprobación, ignore este mensaje.<br>
                            El enlace expira en 24 horas.
                        </p>
                    </div>
                    <div class="footer">
                        <p>Sistema de Firma Digital | © 2025 - Todos los derechos reservados</p>
                    </div>
                </div>
            </body>
            </html>
            """
            
            msg = Message(
                subject=f"🔐 Aprobación requerida: {filename}",
                recipients=[recipient_email],
                html=html_body
            )
            
            current_app.mail.send(msg)
            print(f"✅ Correo profesional enviado a {recipient_email}")
            return True
            
        except Exception as e:
            print(f"❌ Error enviando correo: {e}")
            return False